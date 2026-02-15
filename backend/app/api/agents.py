"""Agent management endpoints."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.agents.base_agent import BaseAgent, AgentConfig, AgentResponse
from app.llm.openai_provider import OpenAIProvider
from app.llm.claude_provider import ClaudeProvider
from app.memory.conversation import ConversationMemory
from app.core.config import settings
from loguru import logger

router = APIRouter()

# In-memory agent store
agent_store: Dict[str, BaseAgent] = {}

class CreateAgentRequest(BaseModel):
    name: str
    description: str = ""
    system_prompt: str = "You are a helpful AI assistant."
    llm_provider: str = "openai"
    model: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 2000

class AgentRunRequest(BaseModel):
    input: str
    context: Optional[Dict[str, Any]] = None

@router.post("/create")
async def create_agent(request: CreateAgentRequest):
    """Create a new agent."""
    try:
        if request.llm_provider == "openai":
            model = request.model or "gpt-4-turbo-preview"
            llm = OpenAIProvider(model=model, api_key=settings.OPENAI_API_KEY)
        elif request.llm_provider == "claude":
            model = request.model or "claude-3-opus-20240229"
            llm = ClaudeProvider(model=model, api_key=settings.ANTHROPIC_API_KEY)
        else:
            raise HTTPException(status_code=400, detail="Invalid LLM provider")
        
        config = AgentConfig(
            name=request.name,
            description=request.description,
            system_prompt=request.system_prompt,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        agent = BaseAgent(config=config, llm_provider=llm, memory=ConversationMemory())
        agent_store[request.name] = agent
        
        logger.info(f"Created agent: {request.name}")
        return {"message": f"Agent {request.name} created successfully", "agent_id": request.name}
    except Exception as e:
        logger.error(f"Error creating agent: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/run/{agent_name}", response_model=AgentResponse)
async def run_agent(agent_name: str, request: AgentRunRequest):
    """Run an agent with input."""
    try:
        if agent_name not in agent_store:
            raise HTTPException(status_code=404, detail=f"Agent {agent_name} not found")
        
        agent = agent_store[agent_name]
        response = await agent.run(request.input, request.context)
        return response
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error running agent: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/list")
async def list_agents():
    """List all agents."""
    return {
        "agents": [
            {"name": name, "description": agent.config.description, "model": agent.llm_provider.model}
            for name, agent in agent_store.items()
        ]
    }

@router.delete("/delete/{agent_name}")
async def delete_agent(agent_name: str):
    """Delete an agent."""
    if agent_name not in agent_store:
        raise HTTPException(status_code=404, detail=f"Agent {agent_name} not found")
    
    del agent_store[agent_name]
    logger.info(f"Deleted agent: {agent_name}")
    return {"message": f"Agent {agent_name} deleted successfully"}
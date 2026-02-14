"""Base agent implementation."""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from app.llm.base import BaseLLMProvider, Message, LLMResponse
from app.tools.base import BaseTool
from app.memory.base import BaseMemory
from loguru import logger

class AgentConfig(BaseModel):
    """Agent configuration."""
    name: str
    description: str = ""
    system_prompt: str = "You are a helpful AI assistant."
    temperature: float = 0.7
    max_tokens: int = 2000

class AgentResponse(BaseModel):
    """Agent response model."""
    output: str
    tool_calls: List[Dict[str, Any]] = []
    tokens_used: int = 0
    model: str = ""

class BaseAgent:
    """Base agent implementation."""
    
    def __init__(self,
        config: AgentConfig,
        llm_provider: BaseLLMProvider,
        tools: Optional[List[BaseTool]] = None,
        memory: Optional[BaseMemory] = None
    ):
        self.config = config
        self.llm_provider = llm_provider
        self.tools = tools or []
        self.memory = memory
        logger.info(f"Initialized agent: {config.name}")
    
    async def run(self, user_input: str, context: Optional[Dict[str, Any]] = None) -> AgentResponse:
        """Execute agent with user input."""
        try:
            # Build message history
            messages = [Message(role="system", content=self.config.system_prompt)]
            
            # Add memory context if available
            if self.memory:
                history = await self.memory.get_history()
                messages.extend(history)
            
            # Add current user message
            messages.append(Message(role="user", content=user_input))
            
            # Generate response
            response = await self.llm_provider.generate(
                messages=messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )
            
            # Store in memory
            if self.memory:
                await self.memory.add_message(Message(role="user", content=user_input))
                await self.memory.add_message(Message(role="assistant", content=response.content))
            
            return AgentResponse(
                output=response.content,
                tokens_used=response.tokens_used,
                model=response.model
            )
        except Exception as e:
            logger.error(f"Agent execution error: {e}")
            raise

"""Multi-agent orchestration system."""
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from app.agents.base_agent import BaseAgent, AgentResponse
from loguru import logger

class OrchestratorConfig(BaseModel):
    """Configuration for multi-agent orchestrator."""
    name: str
    strategy: str = "sequential"

class AgentOrchestrator:
    """Orchestrates multiple agents working together."""
    
    def __init__(self, config: OrchestratorConfig):
        self.config = config
        self.agents: Dict[str, BaseAgent] = {}
        logger.info(f"Initialized orchestrator: {config.name}")
    
    def add_agent(self, name: str, agent: BaseAgent):
        """Add an agent to the orchestrator."""
        self.agents[name] = agent
        logger.info(f"Added agent {name} to orchestrator")
    
    def remove_agent(self, name: str):
        """Remove an agent from the orchestrator."""
        if name in self.agents:
            del self.agents[name]
            logger.info(f"Removed agent {name} from orchestrator")
    
    async def execute_sequential(self, task: str, context: Optional[Dict[str, Any]] = None) -> List[AgentResponse]:
        """Execute agents sequentially."""
        responses = []
        current_input = task
        
        for name, agent in self.agents.items():
            logger.info(f"Executing agent: {name}")
            response = await agent.run(current_input, context)
            responses.append(response)
            current_input = response.output
        
        return responses
    
    async def execute_parallel(self, task: str, context: Optional[Dict[str, Any]] = None) -> List[AgentResponse]:
        """Execute all agents in parallel."""
        import asyncio
        
        tasks = [agent.run(task, context) for agent in self.agents.values()]
        responses = await asyncio.gather(*tasks)
        return list(responses)
    
    async def run(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Run orchestrator based on strategy."""
        logger.info(f"Orchestrator executing with strategy: {self.config.strategy}")
        
        if self.config.strategy == "sequential":
            responses = await self.execute_sequential(task, context)
        elif self.config.strategy == "parallel":
            responses = await self.execute_parallel(task, context)
        else:
            raise ValueError(f"Unknown strategy: {self.config.strategy}")
        
        return {
            "strategy": self.config.strategy,
            "responses": responses,
            "final_output": responses[-1].output if responses else ""
        }
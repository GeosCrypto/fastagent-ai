"""Base tool interface."""
from abc import ABC, abstractmethod
from typing import Any, Dict
from pydantic import BaseModel

class ToolInput(BaseModel):
    """Base tool input model."""
    pass

class ToolOutput(BaseModel):
    """Tool output model."""
    result: Any
    error: str = ""
    success: bool = True

class BaseTool(ABC):
    """Base class for agent tools."""
    
    name: str = "base_tool"
    description: str = "Base tool"
    input_model: type[ToolInput] = ToolInput
    
    @abstractmethod
    async def execute(self, **kwargs) -> ToolOutput:
        """Execute the tool."""
        pass    
    def to_dict(self) -> Dict[str, Any]:
        """Convert tool to dictionary for LLM function calling."""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.input_model.model_json_schema()
        }
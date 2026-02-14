"""Base LLM provider interface."""
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from pydantic import BaseModel

class Message(BaseModel):
    """Message model."""
    role: str
    content: str

class LLMResponse(BaseModel):
    """LLM response model."""
    content: str
    model: str
    tokens_used: int
    finish_reason: Optional[str] = None

class BaseLLMProvider(ABC):
    """Base class for LLM providers."""
    
    def __init__(self, model: str, api_key: str, **kwargs):
        self.model = model
        self.api_key = api_key
        self.kwargs = kwargs
    
    @abstractmethod
    async def generate(
        self,
        messages: List[Message],
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> LLMResponse:
        """Generate a response from the LLM."""
        pass
    
    @abstractmethod
    async def stream(
        self,
        messages: List[Message],
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ):
        """Stream responses from the LLM."""
        pass
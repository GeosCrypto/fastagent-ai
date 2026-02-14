"""Base memory interface."""
from abc import ABC, abstractmethod
from typing import List
from app.llm.base import Message

class BaseMemory(ABC):
    """Base class for agent memory."""
    
    @abstractmethod
    async def add_message(self, message: Message) -> None:
        """Add a message to memory."""
        pass
    
    @abstractmethod
    async def get_history(self) -> List[Message]:
        """Retrieve message history."""
        pass
    
    @abstractmethod
    async def clear(self) -> None:
        """Clear memory."""
        pass

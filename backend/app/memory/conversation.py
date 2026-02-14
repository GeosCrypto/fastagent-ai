"""Conversation memory implementation."""
from typing import List
from app.memory.base import BaseMemory
from app.llm.base import Message

class ConversationMemory(BaseMemory):
    """Simple in-memory conversation storage."""
    
    def __init__(self, max_messages: int = 50):
        self.max_messages = max_messages
        self.messages: List[Message] = []
    
    async def add_message(self, message: Message) -> None:
        """Add message to conversation history."""
        self.messages.append(message)
        
        # Keep only last N messages
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
    
    async def get_history(self) -> List[Message]:
        """Get conversation history."""
        return self.messages.copy()
    
    async def clear(self) -> None:
        """Clear conversation history."""
        self.messages = []

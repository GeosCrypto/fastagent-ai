"""Anthropic Claude LLM provider."""
from typing import List, AsyncIterator
from anthropic import AsyncAnthropic
from app.llm.base import BaseLLMProvider, Message, LLMResponse
from loguru import logger

class ClaudeProvider(BaseLLMProvider):
    """Anthropic Claude provider.""" 
    
    def __init__(self, model: str = "claude-3-opus-20240229", api_key: str = "", **kwargs):
        super().__init__(model, api_key, **kwargs)
        self.client = AsyncAnthropic(api_key=api_key)
    
    async def generate(
        self,
        messages: List[Message],
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> LLMResponse:
        """Generate a response using Claude.""" 
        try:
            # Separate system message from conversation
            system_msg = ""
            conv_messages = []
            
            for msg in messages:
                if msg.role == "system":
                    system_msg = msg.content
                else:
                    conv_messages.append({"role": msg.role, "content": msg.content})
            
            response = await self.client.messages.create(
                model=self.model,
                system=system_msg if system_msg else None,
                messages=conv_messages,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )
            
            return LLMResponse(
                content=response.content[0].text,
                model=response.model,
                tokens_used=response.usage.input_tokens + response.usage.output_tokens,
                finish_reason=response.stop_reason
            )
        except Exception as e:
            logger.error(f"Claude generation error: {e}")
            raise
    
    async def stream(
        self,
        messages: List[Message],
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> AsyncIterator[str]:
        """Stream responses from Claude.""" 
        try:
            system_msg = ""
            conv_messages = []
            
            for msg in messages:
                if msg.role == "system":
                    system_msg = msg.content
                else:
                    conv_messages.append({"role": msg.role, "content": msg.content})
            
            async with self.client.messages.stream(
                model=self.model,
                system=system_msg if system_msg else None,
                messages=conv_messages,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            ) as stream:
                async for text in stream.text_stream:
                    yield text
        except Exception as e:
            logger.error(f"Claude streaming error: {e}")
            raise
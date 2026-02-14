"""OpenAI LLM provider."""
from typing import List, AsyncIterator
from openai import AsyncOpenAI
from app.llm.base import BaseLLMProvider, Message, LLMResponse
from loguru import logger

class OpenAIProvider(BaseLLMProvider):
    """OpenAI GPT provider.""" 
    
    def __init__(self, model: str = "gpt-4-turbo-preview", api_key: str = "", **kwargs):
        super().__init__(model, api_key, **kwargs)
        self.client = AsyncOpenAI(api_key=api_key)
    
    async def generate(
        self,
        messages: List[Message],
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> LLMResponse:
        """Generate a response using OpenAI."""
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": m.role, "content": m.content} for m in messages],
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )
            
            return LLMResponse(
                content=response.choices[0].message.content,
                model=response.model,
                tokens_used=response.usage.total_tokens,
                finish_reason=response.choices[0].finish_reason
            )
        except Exception as e:
            logger.error(f"OpenAI generation error: {e}")
            raise
    
    async def stream(
        self,
        messages: List[Message],
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs
    ) -> AsyncIterator[str]:
        """Stream responses from OpenAI."""
        try:
            stream = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": m.role, "content": m.content} for m in messages],
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True,
                **kwargs
            )
            
            async for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            logger.error(f"OpenAI streaming error: {e}")
            raise
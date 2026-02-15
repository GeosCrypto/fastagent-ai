"""Chat endpoints for conversational interface."""
from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import Optional, List
from app.llm.base import Message
from app.llm.openai_provider import OpenAIProvider
from app.llm.claude_provider import ClaudeProvider
from app.core.config import settings
from loguru import logger

router = APIRouter()

class ChatRequest(BaseModel):
    messages: List[Message]
    provider: str = "openai"
    model: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 2000

class ChatResponse(BaseModel):
    response: str
    model: str
    tokens_used: int

@router.post("/completions", response_model=ChatResponse)
async def chat_completion(request: ChatRequest):
    """Generate a chat completion."""
    try:
        if request.provider == "openai":
            model = request.model or "gpt-4-turbo-preview"
            llm = OpenAIProvider(model=model, api_key=settings.OPENAI_API_KEY)
        elif request.provider == "claude":
            model = request.model or "claude-3-opus-20240229"
            llm = ClaudeProvider(model=model, api_key=settings.ANTHROPIC_API_KEY)
        else:
            raise HTTPException(status_code=400, detail="Invalid provider")
        
        response = await llm.generate(
            messages=request.messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        return ChatResponse(
            response=response.content,
            model=response.model,
            tokens_used=response.tokens_used
        )
    except Exception as e:
        logger.error(f"Chat completion error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.websocket("/stream")
async def chat_stream(websocket: WebSocket):
    """Stream chat responses via WebSocket."""
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            provider = data.get("provider", "openai")
            model = data.get("model")
            messages = [Message(**msg) for msg in data.get("messages", [])]
            temperature = data.get("temperature", 0.7)
            max_tokens = data.get("max_tokens", 2000)
            
            if provider == "openai":
                model = model or "gpt-4-turbo-preview"
                llm = OpenAIProvider(model=model, api_key=settings.OPENAI_API_KEY)
            elif provider == "claude":
                model = model or "claude-3-opus-20240229"
                llm = ClaudeProvider(model=model, api_key=settings.ANTHROPIC_API_KEY)
            else:
                await websocket.send_json({"error": "Invalid provider"})
                continue
            
            async for chunk in llm.stream(messages=messages, temperature=temperature, max_tokens=max_tokens):
                await websocket.send_json({"chunk": chunk})
            
            await websocket.send_json({"done": True})
    except WebSocketDisconnect:
        logger.info("WebSocket disconnected")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")

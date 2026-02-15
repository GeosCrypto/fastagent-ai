"""Code execution tool with safety restrictions."""
from pydantic import BaseModel, Field
from app.tools.base import BaseTool, ToolOutput
from loguru import logger
from io import StringIO
import contextlib

class CodeExecutorInput(BaseModel):
    code: str = Field(description="Python code to execute")
    language: str = Field(default="python", description="Programming language")

class CodeExecutorTool(BaseTool):
    """Safe code execution tool."""
    
    name = "code_executor"
    description = "Execute Python code safely in a restricted environment"
    input_model = CodeExecutorInput
    
    async def execute(self, code: str, language: str = "python") -> ToolOutput:
        """Execute code safely."""
        if language != "python":
            return ToolOutput(result="", error="Only Python is supported", success=False)
        
        try:
            output_buffer = StringIO()
            
            with contextlib.redirect_stdout(output_buffer):
                safe_globals = {
                    "__builtins__": {
                        "print": print,
                        "len": len,
                        "range": range,
                        "list": list,
                        "dict": dict,
                        "str": str,
                        "int": int,
                        "float": float,
                        "sum": sum,
                        "min": min,
                        "max": max,
                    }
                }
                exec(code, safe_globals)
            
            output = output_buffer.getvalue()
            logger.info(f"Code executed successfully")
            return ToolOutput(result=output or "Code executed successfully", success=True)
        except Exception as e:
            logger.error(f"Code execution error: {e}")
            return ToolOutput(result="", error=str(e), success=False)
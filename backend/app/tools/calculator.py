"""Calculator tool implementation."""
from pydantic import BaseModel, Field
from app.tools.base import BaseTool, ToolOutput
from loguru import logger
import ast
import operator

class CalculatorInput(BaseModel):
    expression: str = Field(description="Mathematical expression to evaluate")

class CalculatorTool(BaseTool):
    """Calculator tool for mathematical operations."""
    
    name = "calculator"
    description = "Evaluate mathematical expressions safely"
    input_model = CalculatorInput
    
    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
    }
    
    def _eval_expr(self, node):
        """Safely evaluate expression AST node."""
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return self.OPERATORS[type(node.op)](
                self._eval_expr(node.left),
                self._eval_expr(node.right)
            )
        elif isinstance(node, ast.UnaryOp):
            return self.OPERATORS[type(node.op)](self._eval_expr(node.operand))
        else:
            raise ValueError(f"Unsupported operation: {type(node)}")
    
    async def execute(self, expression: str) -> ToolOutput:
        """Execute calculation."""
        try:
            node = ast.parse(expression, mode='eval')
            result = self._eval_expr(node.body)
            logger.info(f"Calculated: {expression} = {result}")
            return ToolOutput(result=str(result), success=True)
        except Exception as e:
            logger.error(f"Calculator error: {e}")
            return ToolOutput(result="", error=str(e), success=False)
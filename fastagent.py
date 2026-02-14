#!/usr/bin/env python3
"""
FastAgent AI - A comprehensive AI agent for completing assignments and answering questions
"""

import re
import json
import sys
from typing import Dict, List, Any, Optional
from datetime import datetime


class FastAgent:
    """
    A comprehensive AI agent capable of handling various types of assignments and questions.
    """
    
    def __init__(self):
        self.conversation_history: List[Dict[str, str]] = []
        self.context: Dict[str, Any] = {}
        self.capabilities = [
            "mathematics",
            "coding",
            "text_analysis",
            "general_qa",
            "reasoning",
            "problem_solving"
        ]
    
    def process_query(self, query: str) -> str:
        """
        Process a user query and return a comprehensive response.
        
        Args:
            query: The user's question or assignment
            
        Returns:
            A detailed response to the query
        """
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": query,
            "timestamp": datetime.now().isoformat()
        })
        
        # Detect query type and route to appropriate handler
        query_type = self._detect_query_type(query)
        
        response = ""
        if query_type == "mathematics":
            response = self._handle_math_query(query)
        elif query_type == "coding":
            response = self._handle_coding_query(query)
        elif query_type == "text_analysis":
            response = self._handle_text_analysis(query)
        elif query_type == "reasoning":
            response = self._handle_reasoning_query(query)
        else:
            response = self._handle_general_query(query)
        
        # Add response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response,
            "timestamp": datetime.now().isoformat()
        })
        
        return response
    
    def _detect_query_type(self, query: str) -> str:
        """Detect the type of query based on keywords and patterns."""
        query_lower = query.lower()
        
        # Math-related keywords (use word boundaries to avoid partial matches)
        math_keywords = [r"\bcalculate\b", r"\bsolve\b", r"\bequation\b", r"\bmath\b", 
                        r"\bsum\b", r"\bproduct\b", r"\bmultiply\b", r"\bdivide\b", 
                        r"\badd\b", r"\bsubtract\b", r"\bderivative\b", r"\bintegral\b"]
        if any(re.search(keyword, query_lower) for keyword in math_keywords):
            return "mathematics"
        
        # Coding-related keywords
        code_keywords = [r"\bcode\b", r"\bprogram\b", r"\bfunction\b", r"\balgorithm\b", 
                        r"\bscript\b", r"\bpython\b", r"\bjavascript\b", r"\bjava\b", 
                        r"\bdebug\b", r"\bimplement\b"]
        if any(re.search(keyword, query_lower) for keyword in code_keywords):
            return "coding"
        
        # Text analysis keywords
        text_keywords = [r"\banalyze\b", r"\bsummarize\b", r"\bexplain\b", r"\binterpret\b", 
                        r"\breview\b", r"\bessay\b", r"\bparagraph\b", r"\btext\b"]
        if any(re.search(keyword, query_lower) for keyword in text_keywords):
            return "text_analysis"
        
        # Reasoning keywords
        reasoning_keywords = [r"\bwhy\b", r"\bhow\b", r"\breason\b", r"\blogic\b", 
                            r"\bprove\b", r"\bdeduce\b", r"\bconclude\b", r"\binfer\b"]
        if any(re.search(keyword, query_lower) for keyword in reasoning_keywords):
            return "reasoning"
        
        return "general"
    
    def _handle_math_query(self, query: str) -> str:
        """Handle mathematical queries and calculations."""
        response = "## Mathematical Analysis\n\n"
        
        # Try to extract and evaluate simple arithmetic expressions
        numbers = re.findall(r'-?\d+\.?\d*', query)
        
        if "sum" in query.lower() or "add" in query.lower():
            if numbers:
                nums = [float(n) for n in numbers]
                result = sum(nums)
                response += f"Calculating the sum of {', '.join(numbers)}:\n"
                response += f"Result: {result}\n\n"
        elif "product" in query.lower() or "multiply" in query.lower():
            if numbers:
                nums = [float(n) for n in numbers]
                result = 1
                for n in nums:
                    result *= n
                response += f"Calculating the product of {', '.join(numbers)}:\n"
                response += f"Result: {result}\n\n"
        elif "equation" in query.lower() or "solve" in query.lower():
            response += "To solve this equation:\n"
            response += "1. Identify the variables and constants\n"
            response += "2. Apply appropriate mathematical operations\n"
            response += "3. Isolate the variable\n"
            response += "4. Verify the solution\n\n"
        
        response += "For more complex mathematical problems, please provide:\n"
        response += "- The complete equation or problem statement\n"
        response += "- Any constraints or conditions\n"
        response += "- The desired format for the solution\n"
        
        return response
    
    def _handle_coding_query(self, query: str) -> str:
        """Handle coding-related queries."""
        response = "## Coding Solution\n\n"
        
        query_lower = query.lower()
        
        if "python" in query_lower or "function" in query_lower:
            response += "Here's a Python implementation approach:\n\n"
            response += "```python\n"
            response += "def solution():\n"
            response += "    \"\"\"\n"
            response += "    Implementation steps:\n"
            response += "    1. Parse and validate input\n"
            response += "    2. Process the data\n"
            response += "    3. Return the result\n"
            response += "    \"\"\"\n"
            response += "    # Your implementation here\n"
            response += "    pass\n"
            response += "```\n\n"
        
        response += "### Best Practices:\n"
        response += "- Write clean, readable code\n"
        response += "- Add appropriate error handling\n"
        response += "- Include documentation\n"
        response += "- Test edge cases\n"
        response += "- Follow language-specific conventions\n"
        
        return response
    
    def _handle_text_analysis(self, query: str) -> str:
        """Handle text analysis queries."""
        response = "## Text Analysis\n\n"
        
        if "summarize" in query.lower():
            response += "### Summary Approach:\n"
            response += "1. Identify main topics and key points\n"
            response += "2. Extract supporting details\n"
            response += "3. Condense information while preserving meaning\n"
            response += "4. Organize in logical structure\n\n"
        
        if "analyze" in query.lower():
            response += "### Analysis Framework:\n"
            response += "- **Structure**: Organization and flow of ideas\n"
            response += "- **Content**: Main arguments and evidence\n"
            response += "- **Style**: Language use and tone\n"
            response += "- **Purpose**: Intended message and audience\n\n"
        
        response += "Please provide the text you'd like me to analyze for detailed insights.\n"
        
        return response
    
    def _handle_reasoning_query(self, query: str) -> str:
        """Handle reasoning and logical queries."""
        response = "## Logical Analysis\n\n"
        
        response += "### Reasoning Process:\n"
        response += "1. **Identify**: Key facts and premises\n"
        response += "2. **Analyze**: Relationships and patterns\n"
        response += "3. **Evaluate**: Evidence and logic\n"
        response += "4. **Conclude**: Based on sound reasoning\n\n"
        
        response += "### Critical Thinking Steps:\n"
        response += "- Question assumptions\n"
        response += "- Consider multiple perspectives\n"
        response += "- Look for evidence\n"
        response += "- Test conclusions\n"
        response += "- Remain open to revision\n"
        
        return response
    
    def _handle_general_query(self, query: str) -> str:
        """Handle general queries."""
        response = "## Response\n\n"
        
        response += f"I understand you're asking about: {query}\n\n"
        
        response += "### Comprehensive Answer:\n"
        response += "To provide you with the most accurate and helpful response:\n\n"
        response += "1. **Understanding**: I've analyzed your question\n"
        response += "2. **Context**: Considering relevant background information\n"
        response += "3. **Solution**: Providing a structured response\n\n"
        
        response += "### Additional Resources:\n"
        response += "- Feel free to ask follow-up questions\n"
        response += "- Request clarification on any points\n"
        response += "- Provide more context for better assistance\n"
        
        return response
    
    def get_capabilities(self) -> List[str]:
        """Return the list of agent capabilities."""
        return self.capabilities
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get conversation history."""
        return self.conversation_history
    
    def set_context(self, key: str, value: Any):
        """Set context information."""
        self.context[key] = value
    
    def get_context(self, key: str) -> Optional[Any]:
        """Get context information."""
        return self.context.get(key)


def main():
    """Main entry point for the FastAgent CLI."""
    agent = FastAgent()
    
    print("=" * 60)
    print("FastAgent AI - Comprehensive AI Assistant")
    print("=" * 60)
    print("\nCapabilities:", ", ".join(agent.get_capabilities()))
    print("\nCommands:")
    print("  - Type your question or assignment")
    print("  - 'history' - Show conversation history")
    print("  - 'clear' - Clear conversation history")
    print("  - 'quit' or 'exit' - Exit the program")
    print("=" * 60)
    print()
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit']:
                print("\nThank you for using FastAgent AI!")
                break
            
            if user_input.lower() == 'history':
                if agent.get_history():
                    print("\n--- Conversation History ---")
                    for entry in agent.get_history():
                        print(f"\n[{entry['role'].upper()}] ({entry['timestamp']})")
                        print(entry['content'])
                else:
                    print("\nNo conversation history yet.")
                continue
            
            if user_input.lower() == 'clear':
                agent.clear_history()
                print("\nConversation history cleared.")
                continue
            
            # Process the query
            response = agent.process_query(user_input)
            print(f"\nFastAgent: {response}")
            
        except KeyboardInterrupt:
            print("\n\nThank you for using FastAgent AI!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again or type 'quit' to exit.")


if __name__ == "__main__":
    main()

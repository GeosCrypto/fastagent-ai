#!/usr/bin/env python3
"""
Test suite for FastAgent AI
"""

import unittest
from fastagent import FastAgent


class TestFastAgent(unittest.TestCase):
    """Test cases for FastAgent functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.agent = FastAgent()
    
    def test_initialization(self):
        """Test agent initialization."""
        self.assertIsInstance(self.agent, FastAgent)
        self.assertEqual(len(self.agent.get_history()), 0)
        self.assertTrue(len(self.agent.get_capabilities()) > 0)
    
    def test_capabilities(self):
        """Test agent capabilities are properly defined."""
        capabilities = self.agent.get_capabilities()
        expected_capabilities = [
            "mathematics",
            "coding",
            "text_analysis",
            "general_qa",
            "reasoning",
            "problem_solving"
        ]
        for cap in expected_capabilities:
            self.assertIn(cap, capabilities)
    
    def test_detect_math_query(self):
        """Test detection of mathematical queries."""
        math_queries = [
            "Calculate 5 + 10",
            "Solve this equation",
            "What is the sum of 15 and 20?",
            "Multiply 3 by 7"
        ]
        for query in math_queries:
            query_type = self.agent._detect_query_type(query)
            self.assertEqual(query_type, "mathematics")
    
    def test_detect_coding_query(self):
        """Test detection of coding queries."""
        coding_queries = [
            "Write a Python function",
            "How do I implement a sorting algorithm?",
            "Debug this code",
            "Create a JavaScript program"
        ]
        for query in coding_queries:
            query_type = self.agent._detect_query_type(query)
            self.assertEqual(query_type, "coding")
    
    def test_detect_text_analysis_query(self):
        """Test detection of text analysis queries."""
        text_queries = [
            "Analyze this paragraph",
            "Summarize the following text",
            "Explain this essay",
            "Review this document"
        ]
        for query in text_queries:
            query_type = self.agent._detect_query_type(query)
            self.assertEqual(query_type, "text_analysis")
    
    def test_detect_reasoning_query(self):
        """Test detection of reasoning queries."""
        reasoning_queries = [
            "Why is the sky blue?",
            "How does photosynthesis work?",
            "Prove this theorem",
            "What is the reason for climate change?"
        ]
        for query in reasoning_queries:
            query_type = self.agent._detect_query_type(query)
            self.assertEqual(query_type, "reasoning")
    
    def test_process_math_query(self):
        """Test processing of mathematical queries."""
        response = self.agent.process_query("Calculate the sum of 5 and 10")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        self.assertIn("Mathematical", response)
    
    def test_process_coding_query(self):
        """Test processing of coding queries."""
        response = self.agent.process_query("Write a Python function")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        self.assertIn("Coding", response)
    
    def test_process_general_query(self):
        """Test processing of general queries."""
        response = self.agent.process_query("What is artificial intelligence?")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_conversation_history(self):
        """Test conversation history tracking."""
        self.assertEqual(len(self.agent.get_history()), 0)
        
        self.agent.process_query("Test query 1")
        self.assertEqual(len(self.agent.get_history()), 2)  # User + Assistant
        
        self.agent.process_query("Test query 2")
        self.assertEqual(len(self.agent.get_history()), 4)  # 2 * (User + Assistant)
    
    def test_clear_history(self):
        """Test clearing conversation history."""
        self.agent.process_query("Test query")
        self.assertTrue(len(self.agent.get_history()) > 0)
        
        self.agent.clear_history()
        self.assertEqual(len(self.agent.get_history()), 0)
    
    def test_context_management(self):
        """Test context setting and retrieval."""
        self.agent.set_context("test_key", "test_value")
        self.assertEqual(self.agent.get_context("test_key"), "test_value")
        
        self.agent.set_context("number", 42)
        self.assertEqual(self.agent.get_context("number"), 42)
        
        self.assertIsNone(self.agent.get_context("nonexistent_key"))
    
    def test_math_sum_calculation(self):
        """Test simple sum calculation."""
        response = self.agent.process_query("What is the sum of 5, 10, and 15?")
        self.assertIn("30", response)
    
    def test_math_product_calculation(self):
        """Test simple product calculation."""
        response = self.agent.process_query("What is the product of 5 and 6?")
        self.assertIn("30", response)
    
    def test_response_structure(self):
        """Test that responses have proper structure."""
        response = self.agent.process_query("Test query")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 10)  # Should be a meaningful response
    
    def test_history_timestamps(self):
        """Test that history entries have timestamps."""
        self.agent.process_query("Test query")
        history = self.agent.get_history()
        
        for entry in history:
            self.assertIn("timestamp", entry)
            self.assertIn("role", entry)
            self.assertIn("content", entry)
    
    def test_multiple_queries_same_type(self):
        """Test handling multiple queries of the same type."""
        self.agent.process_query("Calculate 5 + 10")
        self.agent.process_query("Calculate 20 + 30")
        
        history = self.agent.get_history()
        self.assertEqual(len(history), 4)  # 2 queries * 2 (user + assistant)
    
    def test_mixed_query_types(self):
        """Test handling different query types in sequence."""
        self.agent.process_query("Calculate 5 + 10")
        self.agent.process_query("Write a Python function")
        self.agent.process_query("Why is water wet?")
        
        history = self.agent.get_history()
        self.assertEqual(len(history), 6)  # 3 queries * 2
    
    def test_empty_query_handling(self):
        """Test that agent handles queries gracefully."""
        try:
            response = self.agent.process_query("")
            self.assertIsInstance(response, str)
        except Exception as e:
            self.fail(f"Agent should handle empty queries without crashing: {e}")
    
    def test_special_characters_in_query(self):
        """Test handling queries with special characters."""
        response = self.agent.process_query("What is 5 + 10 = ?")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)


class TestQueryDetection(unittest.TestCase):
    """Test cases for query type detection."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.agent = FastAgent()
    
    def test_case_insensitive_detection(self):
        """Test that query detection is case-insensitive."""
        query_lower = "calculate the sum"
        query_upper = "CALCULATE THE SUM"
        query_mixed = "CaLcUlAtE tHe SuM"
        
        self.assertEqual(
            self.agent._detect_query_type(query_lower),
            self.agent._detect_query_type(query_upper)
        )
        self.assertEqual(
            self.agent._detect_query_type(query_lower),
            self.agent._detect_query_type(query_mixed)
        )
    
    def test_ambiguous_queries(self):
        """Test handling of ambiguous queries."""
        # Query with multiple potential types
        response = self.agent.process_query("Explain how to code a calculator")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)


class TestAgentResponses(unittest.TestCase):
    """Test cases for agent response quality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.agent = FastAgent()
    
    def test_math_response_completeness(self):
        """Test that math responses are complete."""
        response = self.agent._handle_math_query("Calculate 5 + 10")
        self.assertIn("Mathematical", response)
        self.assertTrue(len(response) > 50)  # Should be detailed
    
    def test_coding_response_completeness(self):
        """Test that coding responses are complete."""
        response = self.agent._handle_coding_query("Write a Python function")
        self.assertIn("Coding", response)
        self.assertIn("python", response.lower())
    
    def test_text_analysis_response_completeness(self):
        """Test that text analysis responses are complete."""
        response = self.agent._handle_text_analysis("Analyze this text")
        self.assertIn("Analysis", response)
        self.assertTrue(len(response) > 50)
    
    def test_reasoning_response_completeness(self):
        """Test that reasoning responses are complete."""
        response = self.agent._handle_reasoning_query("Why is the sky blue?")
        self.assertIn("Reasoning", response)
        self.assertTrue(len(response) > 50)


def run_tests():
    """Run all tests."""
    unittest.main(verbosity=2)


if __name__ == "__main__":
    run_tests()

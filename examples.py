#!/usr/bin/env python3
"""
Examples demonstrating FastAgent AI capabilities
"""

from fastagent import FastAgent


def example_mathematics():
    """Example: Mathematical queries"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Mathematics")
    print("="*60)
    
    agent = FastAgent()
    
    queries = [
        "Calculate the sum of 15, 25, and 35",
        "What is the product of 7 and 8?",
        "Solve this equation: 2x + 5 = 15"
    ]
    
    for query in queries:
        print(f"\nUser: {query}")
        response = agent.process_query(query)
        print(f"\nFastAgent:\n{response}")
        print("-" * 60)


def example_coding():
    """Example: Coding queries"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Coding")
    print("="*60)
    
    agent = FastAgent()
    
    queries = [
        "Write a Python function to check if a number is prime",
        "How do I implement a binary search algorithm?",
        "Debug a sorting function"
    ]
    
    for query in queries:
        print(f"\nUser: {query}")
        response = agent.process_query(query)
        print(f"\nFastAgent:\n{response}")
        print("-" * 60)


def example_text_analysis():
    """Example: Text analysis queries"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Text Analysis")
    print("="*60)
    
    agent = FastAgent()
    
    queries = [
        "Analyze the structure of a persuasive essay",
        "Summarize the key points of an article",
        "Explain the main themes in a paragraph"
    ]
    
    for query in queries:
        print(f"\nUser: {query}")
        response = agent.process_query(query)
        print(f"\nFastAgent:\n{response}")
        print("-" * 60)


def example_reasoning():
    """Example: Reasoning queries"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Reasoning and Logic")
    print("="*60)
    
    agent = FastAgent()
    
    queries = [
        "Why do objects fall to the ground?",
        "How does supply and demand work?",
        "What is the logical conclusion of this argument?"
    ]
    
    for query in queries:
        print(f"\nUser: {query}")
        response = agent.process_query(query)
        print(f"\nFastAgent:\n{response}")
        print("-" * 60)


def example_context_management():
    """Example: Using context for specialized tasks"""
    print("\n" + "="*60)
    print("EXAMPLE 5: Context Management")
    print("="*60)
    
    agent = FastAgent()
    
    # Set context for specialized domain
    agent.set_context("domain", "mathematics")
    agent.set_context("difficulty", "advanced")
    
    print(f"\nContext set: domain={agent.get_context('domain')}, "
          f"difficulty={agent.get_context('difficulty')}")
    
    query = "Solve a complex equation"
    print(f"\nUser: {query}")
    response = agent.process_query(query)
    print(f"\nFastAgent:\n{response}")


def example_conversation_flow():
    """Example: Multi-turn conversation"""
    print("\n" + "="*60)
    print("EXAMPLE 6: Conversation Flow")
    print("="*60)
    
    agent = FastAgent()
    
    conversation = [
        "What is Python?",
        "How do I write a function in Python?",
        "Can you show me an example?",
        "What are best practices?"
    ]
    
    for query in conversation:
        print(f"\nUser: {query}")
        response = agent.process_query(query)
        print(f"\nFastAgent: {response}")
        print("-" * 40)
    
    # Show conversation history
    print("\n" + "="*60)
    print("CONVERSATION HISTORY")
    print("="*60)
    history = agent.get_history()
    print(f"\nTotal exchanges: {len(history) // 2}")
    print(f"Total messages: {len(history)}")


def example_batch_processing():
    """Example: Processing multiple queries efficiently"""
    print("\n" + "="*60)
    print("EXAMPLE 7: Batch Processing")
    print("="*60)
    
    agent = FastAgent()
    
    queries = [
        ("Math", "Calculate 100 + 200"),
        ("Code", "Write a Hello World program"),
        ("Reason", "Why is learning important?"),
        ("Analysis", "Analyze a short paragraph"),
        ("General", "What is artificial intelligence?")
    ]
    
    print("\nProcessing multiple queries:")
    results = []
    
    for category, query in queries:
        response = agent.process_query(query)
        results.append({
            "category": category,
            "query": query,
            "response_length": len(response),
            "success": len(response) > 0
        })
    
    print("\nResults Summary:")
    print("-" * 60)
    for result in results:
        status = "✓" if result["success"] else "✗"
        print(f"{status} [{result['category']}] {result['query'][:40]}...")
        print(f"  Response length: {result['response_length']} characters")


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("FastAgent AI - Usage Examples")
    print("="*60)
    
    examples = [
        ("Mathematics", example_mathematics),
        ("Coding", example_coding),
        ("Text Analysis", example_text_analysis),
        ("Reasoning", example_reasoning),
        ("Context Management", example_context_management),
        ("Conversation Flow", example_conversation_flow),
        ("Batch Processing", example_batch_processing)
    ]
    
    print("\nAvailable examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")
    
    print("\nRunning all examples...")
    print("="*60)
    
    for name, example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"\nError in {name}: {str(e)}")
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("="*60)


if __name__ == "__main__":
    main()

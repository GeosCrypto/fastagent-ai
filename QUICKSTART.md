# FastAgent AI - Quick Start Guide

## What is FastAgent AI?

FastAgent AI is a comprehensive, fully functional AI agent designed to respond to and complete various types of assignments and questions. It uses intelligent query classification to route requests to specialized handlers for optimal responses.

## Quick Start (5 minutes)

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/GeosCrypto/fastagent-ai.git
cd fastagent-ai

# Run directly (no installation needed!)
python fastagent.py
```

### 2. First Interaction

```
You: Calculate the sum of 10, 20, and 30
FastAgent: [Provides calculation: Result: 60.0]

You: Write a Python function to reverse a string
FastAgent: [Provides code structure and best practices]

You: Why is the sky blue?
FastAgent: [Provides logical reasoning and explanation]
```

### 3. Key Commands

- **Type any question** - Get a response
- **`history`** - View conversation history
- **`clear`** - Clear history
- **`quit`** - Exit

## What Can It Do?

### 1. Mathematics
- Arithmetic calculations (sum, product, etc.)
- Equation solving guidance
- Mathematical reasoning

**Example:**
```
You: What is the product of 12 and 15?
FastAgent: Result: 180.0
```

### 2. Coding
- Algorithm design
- Code structure suggestions
- Implementation guidance
- Best practices

**Example:**
```
You: Write a function to find prime numbers
FastAgent: [Provides Python implementation template]
```

### 3. Text Analysis
- Summarization frameworks
- Content analysis
- Essay structure guidance

**Example:**
```
You: Analyze this paragraph structure
FastAgent: [Provides analysis framework]
```

### 4. Logical Reasoning
- Critical thinking steps
- Cause and effect analysis
- Logical conclusions

**Example:**
```
You: Why do leaves change color in fall?
FastAgent: [Provides reasoning process]
```

### 5. General Q&A
- Comprehensive answers to any question
- Structured responses
- Follow-up support

## Using as a Library

```python
from fastagent import FastAgent

# Create agent
agent = FastAgent()

# Process queries
response = agent.process_query("Calculate 5 + 10")
print(response)

# View capabilities
print(agent.get_capabilities())

# Manage context
agent.set_context("domain", "mathematics")

# Access history
history = agent.get_history()
```

## Examples

Run the examples file to see all capabilities in action:

```bash
python examples.py
```

This demonstrates:
- Mathematical queries
- Coding queries
- Text analysis
- Reasoning
- Context management
- Conversation flow
- Batch processing

## Testing

Run the comprehensive test suite:

```bash
python test_fastagent.py
```

**26 tests covering:**
- Query detection
- Response generation
- History management
- Context handling
- Edge cases

## Architecture Overview

```
User Query → Query Detection → Handler Selection → Response Generation
                                                          ↓
                                              Conversation History
```

**Components:**
1. **FastAgent Class**: Main controller
2. **Query Detection**: Pattern-based classification
3. **Specialized Handlers**: Domain-specific processing
4. **History Tracking**: Complete conversation logs
5. **Context Manager**: State maintenance

## Features

✓ No external dependencies (pure Python)
✓ 26 comprehensive tests (all passing)
✓ Interactive CLI interface
✓ Conversation history tracking
✓ Context management
✓ Extensible architecture
✓ Clean, documented code
✓ MIT licensed

## Next Steps

1. **Explore**: Run `python fastagent.py` and try different queries
2. **Examples**: Run `python examples.py` to see all capabilities
3. **Test**: Run `python test_fastagent.py` to verify installation
4. **Extend**: See CONTRIBUTING.md for adding new capabilities
5. **Integrate**: Import as a library in your projects

## Common Use Cases

### For Students
- Homework assistance
- Concept explanations
- Problem-solving guidance
- Study support

### For Developers
- Code structure guidance
- Algorithm design help
- Best practices
- Quick prototyping

### For Learning
- Step-by-step reasoning
- Multiple domain support
- Interactive exploration
- Progressive understanding

## Troubleshooting

**Q: Nothing happens when I run fastagent.py**
A: Make sure Python 3.7+ is installed: `python3 --version`

**Q: How do I exit?**
A: Type `quit` or `exit`, or press Ctrl+C

**Q: Can I use this in my project?**
A: Yes! It's MIT licensed and can be imported as a library.

**Q: How accurate are the responses?**
A: The agent provides structured frameworks and guidance. For specific calculations, it performs arithmetic operations. For complex topics, it provides reasoning frameworks and best practices.

## Support

- **Issues**: [GitHub Issues](https://github.com/GeosCrypto/fastagent-ai/issues)
- **Documentation**: [README.md](README.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License - See [LICENSE](LICENSE) file

---

**Ready to start?**

```bash
python fastagent.py
```

Welcome to FastAgent AI! 🚀

# FastAgent AI

A comprehensive, fully functional AI agent capable of responding to and completing all types of assignments and questions.

[![Tests](https://img.shields.io/badge/tests-26%20passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()

**🚀 [Quick Start Guide](QUICKSTART.md)** | [Examples](examples.py) | [Contributing](CONTRIBUTING.md)

## Features

- **Multi-Domain Support**: Handles mathematics, coding, text analysis, reasoning, and general Q&A
- **Context Awareness**: Maintains conversation history for coherent multi-turn interactions
- **Intelligent Query Routing**: Automatically detects query type and applies appropriate processing
- **Comprehensive Responses**: Provides structured, detailed answers with explanations
- **Interactive CLI**: User-friendly command-line interface for easy interaction
- **Extensible Architecture**: Easy to add new capabilities and handlers

## Capabilities

1. **Mathematics**: Arithmetic calculations, equation solving, mathematical reasoning
2. **Coding**: Algorithm design, code implementation, debugging assistance
3. **Text Analysis**: Summarization, interpretation, content analysis
4. **Reasoning**: Logical analysis, critical thinking, problem-solving
5. **General Q&A**: Comprehensive responses to any question

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/GeosCrypto/fastagent-ai.git
cd fastagent-ai
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Run the interactive agent:
```bash
python fastagent.py
```

### Commands

- Type any question or assignment to get a response
- `history` - View conversation history
- `clear` - Clear conversation history
- `quit` or `exit` - Exit the program

### Example Interactions

#### Mathematical Query
```
You: Calculate the sum of 15, 23, and 42
FastAgent: [Provides calculation and result]
```

#### Coding Query
```
You: Write a Python function to find prime numbers
FastAgent: [Provides code implementation and explanation]
```

#### Text Analysis
```
You: Analyze this paragraph: [your text]
FastAgent: [Provides structured analysis]
```

#### Reasoning Query
```
You: Why is the sky blue?
FastAgent: [Provides logical explanation with reasoning]
```

### Using as a Library

```python
from fastagent import FastAgent

# Create an agent instance
agent = FastAgent()

# Process a query
response = agent.process_query("Calculate 5 + 10")
print(response)

# Get conversation history
history = agent.get_history()

# Set context for specialized tasks
agent.set_context("domain", "mathematics")
```

## Architecture

### Core Components

1. **FastAgent Class**: Main agent class with query processing logic
2. **Query Detection**: Intelligent classification of user queries
3. **Specialized Handlers**: Domain-specific processing methods
4. **Context Management**: Maintains state across interactions
5. **History Tracking**: Records all conversations with timestamps

### Query Processing Flow

1. User submits a query
2. Agent detects query type (math, coding, text analysis, etc.)
3. Routes to appropriate handler
4. Handler processes and generates response
5. Response is added to conversation history
6. User receives comprehensive answer

## Extensibility

To add new capabilities:

1. Add new capability to `self.capabilities` list
2. Add keywords to `_detect_query_type()` method
3. Create new handler method (e.g., `_handle_new_type()`)
4. Add routing logic in `process_query()` method

Example:
```python
def _handle_translation_query(self, query: str) -> str:
    """Handle language translation queries."""
    response = "## Translation\n\n"
    # Add translation logic here
    return response
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Testing

Run the test suite:
```bash
python test_fastagent.py
```

## License

This project is open source and available under the MIT License.

## Support

For questions, issues, or feature requests:
- Open an issue on GitHub
- Contact: [repository maintainers]

## Roadmap

- [ ] Enhanced mathematical computation with symbolic math
- [ ] Integration with external AI models for improved responses
- [ ] Web interface for browser-based interaction
- [ ] API endpoint for programmatic access
- [ ] Support for file uploads and document processing
- [ ] Multi-language support
- [ ] Voice interaction capabilities
- [ ] Export conversation history to various formats

## Acknowledgments

Built with Python and designed for comprehensive AI-assisted learning and problem-solving.

# Contributing to FastAgent AI

Thank you for your interest in contributing to FastAgent AI! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in the GitHub issue tracker
2. If not, create a new issue with:
   - A clear, descriptive title
   - Detailed description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment details (OS, Python version, etc.)

### Submitting Changes

1. **Fork the repository**
   - Click the "Fork" button on GitHub
   - Clone your fork locally

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed
   - Keep commits focused and atomic

4. **Test your changes**
   ```bash
   python test_fastagent.py
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add feature: brief description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear description of your changes

## Code Style Guidelines

### Python Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small
- Use type hints where appropriate

Example:
```python
def process_query(self, query: str) -> str:
    """
    Process a user query and return a response.
    
    Args:
        query: The user's question or assignment
        
    Returns:
        A detailed response to the query
    """
    # Implementation here
    pass
```

### Documentation

- Update README.md for user-facing changes
- Add docstrings for all new functions and classes
- Include examples for new features
- Keep documentation clear and concise

### Testing

- Add tests for all new functionality
- Ensure all existing tests pass
- Aim for high test coverage
- Test edge cases and error conditions

Example test:
```python
def test_new_feature(self):
    """Test description."""
    agent = FastAgent()
    result = agent.new_feature("input")
    self.assertEqual(result, "expected_output")
```

## Adding New Capabilities

To add a new capability to the agent:

1. **Update the capabilities list**
   ```python
   self.capabilities = [
       # ... existing capabilities
       "new_capability"
   ]
   ```

2. **Add detection keywords**
   ```python
   new_keywords = [r"\bnew\b", r"\bcapability\b"]
   if any(re.search(keyword, query_lower) for keyword in new_keywords):
       return "new_capability"
   ```

3. **Create a handler method**
   ```python
   def _handle_new_capability(self, query: str) -> str:
       """Handle new capability queries."""
       response = "## New Capability\n\n"
       # Add logic here
       return response
   ```

4. **Add routing logic**
   ```python
   if query_type == "new_capability":
       response = self._handle_new_capability(query)
   ```

5. **Add tests**
   ```python
   def test_new_capability(self):
       """Test new capability."""
       agent = FastAgent()
       response = agent.process_query("test query")
       self.assertIn("New Capability", response)
   ```

6. **Update documentation**
   - Add to README.md capabilities section
   - Add examples to examples.py

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/GeosCrypto/fastagent-ai.git
   cd fastagent-ai
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests to verify setup**
   ```bash
   python test_fastagent.py
   ```

## Questions?

If you have questions about contributing:

- Open an issue for discussion
- Tag it with "question"
- Provide context about what you're trying to do

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Maintain a positive environment

Thank you for contributing to FastAgent AI!

# FAST AI - Multi-Agent AI Platform

🚀 **A production-ready, multi-LLM agentic AI framework for building intelligent autonomous agents**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue)](https://www.typescriptlang.org/)

## 🌟 Features

- **Multi-LLM Support**: Seamlessly switch between OpenAI, Anthropic Claude, and other providers
- **Agent Orchestration**: Build complex multi-agent systems with memory and state management
- **Tool Integration**: Extensible tool/function calling framework
- **Production Ready**: FastAPI backend with TypeScript/React frontend
- **Vector Database**: Built-in RAG (Retrieval Augmented Generation) support
- **Monitoring & Logging**: Comprehensive observability for agent actions
- **Type-Safe**: Full TypeScript and Python type safety

## 🏗️ Architecture

```
fastagent-ai/
├── backend/              # Python FastAPI service
│   ├── app/
│   │   ├── agents/       # Agent implementations
│   │   ├── core/         # Core agent engine
│   │   ├── llm/          # LLM providers abstraction
│   │   ├── tools/        # Agent tools/functions
│   │   ├── memory/       # Memory & state management
│   │   └── api/          # REST API endpoints
│   └── tests/
├── frontend/             # TypeScript/React UI
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── public/
├── agents/               # Pre-built agent templates
├── docs/                 # Documentation
└── examples/             # Usage examples
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker (optional)

### Installation

#### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Frontend Setup

```bash
cd frontend
npm install
```

### Configuration

Create a `.env` file in the backend directory:

```env
# LLM Provider API Keys
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

# Database
DATABASE_URL=sqlite:///./fastagent.db

# Vector Database (optional)
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENVIRONMENT=your_environment

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=http://localhost:3000
```

### Running the Application

#### Start Backend

```bash
cd backend
uvicorn app.main:app --reload
```

#### Start Frontend

```bash
cd frontend
npm run dev
```

Access the application at `http://localhost:3000`

## 📖 Usage Examples

### Creating a Simple Agent

```python
from fastagent.core import Agent
from fastagent.llm import OpenAIProvider
from fastagent.tools import WebSearchTool, CalculatorTool

# Initialize agent
agent = Agent(
    name="research_assistant",
    llm_provider=OpenAIProvider(model="gpt-4"),
    tools=[WebSearchTool(), CalculatorTool()],
    system_prompt="You are a helpful research assistant."
)

# Run agent
response = await agent.run(
    "Research the latest developments in quantum computing and summarize the findings."
)

print(response.output)
```

## 🤝 Contributing

We welcome contributions! Please see CONTRIBUTING.md for guidelines.

## 📄 License

MIT License - see LICENSE for details.

---

**Built with ❤️ by the FAST AI team**
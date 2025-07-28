# AI Assistant with LangChain and LangGraph

A Python project demonstrating the integration of LangChain and LangGraph to create intelligent AI assistants with workflow orchestration capabilities.

## 🚀 Features

- **LangChain Integration**: Utilizes LangChain for building LLM-powered applications
- **LangGraph Workflows**: Implements state-based workflow orchestration with LangGraph
- **OpenAI Integration**: Connects to OpenAI's GPT models for natural language processing
- **Translation Service**: Includes a French translation example using LangChain chains
- **State Management**: Demonstrates state-based workflow execution with typed state schemas

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-assistant-langchain-langgraph
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 📁 Project Structure

```
ai-assistant-langchain-langgraph/
├── translator.py        # LangChain translation example
├── dispatcher.py        # LangGraph workflow example
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 🔧 Dependencies

- **langchain**: Core LangChain framework for building LLM applications
- **langchain-community**: Community-contributed LangChain integrations
- **langchain-openai**: OpenAI integration for LangChain
- **langgraph**: Workflow orchestration framework
- **openai**: Official OpenAI Python client
- **python-dotenv**: Environment variable management

### LangChain
- **Chains**: Composable sequences of operations
- **Prompts**: Templates for generating structured inputs to LLMs
- **LLMs**: Language model interfaces

### LangGraph
- **StateGraph**: Graph-based workflow orchestration
- **Nodes**: Individual processing steps in the workflow
- **Edges**: Connections between nodes defining execution flow
- **State**: Typed data structure passed between nodes

## ⚠️ Important Notes

- Ensure you have sufficient OpenAI API credits
- Keep your API keys secure and never commit them to version control
- The examples use GPT-4o model; adjust according to your needs and budget

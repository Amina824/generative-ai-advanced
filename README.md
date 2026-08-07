# 🚀 GenAI Advanced

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LangChain-Advanced-1C3C3C?style=flat-square&logo=langchain&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/OpenAI-API-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/status-actively%20learning-brightgreen?style=flat-square" alt="Status">
</p>

<p align="center">
  A hands-on, project-based journey through <b>advanced Generative AI</b> concepts using <b>LangChain</b> and <b>Large Language Models (LLMs)</b> — built one working example at a time.
</p>

---

## 📖 About

This repository documents my learning journey through advanced GenAI engineering — going beyond "hello world" LLM calls into the architecture, patterns, and tooling used to build production-grade AI applications.

Every topic below is backed by runnable code, not just notes. The goal is to build a strong mental model of **how** and **why** each LangChain primitive works, not just how to call it.

---

## 📚 Topics Covered

### 🤖 Models
Core interface layer connecting applications to LLMs.
| Concept | Description |
|---|---|
| Chat Models | Interacting with conversational LLM interfaces |
| Model Configuration | Setting up providers, keys, and runtime options |
| Temperature & Parameters | Controlling randomness, creativity, and determinism |
| Model Invocation | Sync/async invocation patterns |
| Multiple LLM Providers | Swapping between OpenAI and other providers |

### ✍️ Prompt Engineering
Designing instructions that reliably steer LLM behavior.
- Prompt Templates
- Chat Prompt Templates
- System / Human / AI Messages
- Static Prompts
- Dynamic Prompts (variable injection)

### 📦 Structured Output
Turning free-text generation into reliable, typed data.
- JSON Output
- Pydantic Output Parsing
- Structured Output Schemas
- Output Parsers
- Schema Validation

### 🔗 Chains
Composing multiple LLM calls into coherent pipelines.
- Sequential Chains
- Parallel Chains
- Conditional Chains

### ⚙️ Runnables
LangChain's core composition primitives (LCEL).
- Runnable Interface
- `RunnableLambda`
- `RunnableSequence`
- `RunnableParallel`
- `RunnablePassthrough`
- `RunnableBranch` (Conditional Logic)
- Building Modular AI Pipelines

### 📄 Document Loaders
Ingesting external data into LLM-ready formats.
- `TextLoader`
- `PyPDFLoader`
- `DirectoryLoader`
- `CSVLoader`

---

## 🗺️ Roadmap

Topics planned as this repo grows:

- [ ] Embeddings
- [ ] Vector Databases
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Retrievers
- [ ] Tools
- [ ] AI Agents
- [ ] LangGraph
- [ ] Model Context Protocol (MCP)
- [ ] Memory
- [ ] Streaming
- [ ] Multi-Agent Systems
- [ ] Evaluation
- [ ] Deployment

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core language |
| **LangChain** | LLM orchestration framework |
| **OpenAI** | LLM provider |
| **Pydantic** | Data validation & structured output |
| **python-dotenv** | Environment variable management |

---

## 📁 Project Structure

```text
GenAI-Advanced/
│
├── Models/              # Chat model setup, config, invocation examples
├── Prompts/              # Prompt templates and message types
├── Structured_Output/    # Pydantic + JSON output parsing
├── Chains/                # Sequential, parallel & conditional chains
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Amina824/GenAI-Advanced.git
```

### 2. Navigate to the project
```bash
cd GenAI-Advanced
```

### 3. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Set up environment variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_api_key
```

### 6. Run an example
```bash
python Models/chat_model_example.py
```

---

## 🎯 Learning Objectives

- ✅ Learn advanced LangChain concepts through practical code
- ✅ Understand how production LLM applications are architected
- ✅ Master prompt engineering techniques
- ✅ Generate reliable, validated structured outputs
- ✅ Build modular, composable AI workflows using chains and runnables
- ✅ Progress toward RAG, agents, and multi-agent systems

---

## 🤝 Contributing

This is primarily a personal learning repo, but suggestions, corrections, and discussions are welcome — feel free to open an issue or submit a PR.

---

## 👩‍💻 Author

**Amina Bibi**

---

## ⭐ Support

If this repository helped you understand LangChain or GenAI concepts, consider giving it a **star** — it helps others find it too!

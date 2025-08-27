# GenAI Playground – OpenAI SDK, Prompt Engineering & Terminal Agent  

This repository is a collection of experiments and projects demonstrating the practical use of **Generative AI**, **OpenAI SDK**, and **prompt engineering**.  
It starts from simple chat-based assistants and evolves into a full-fledged **Terminal AI Agent** capable of writing, executing, and deploying code autonomously.  

---

## 📂 Project Structure  

- **`openai_chat.py`** – Basic usage of OpenAI SDK with zero-shot prompting.  
- **`chat_1.py`** – Simple AI assistant responding to generic user queries.  
- **`chat_2.py`** – Domain-restricted assistant (Math-focused, rejects irrelevant questions).  
- **`chat_3.py`** – Chain-of-Thought simulation with structured step-by-step reasoning (`analyse → think → result → validate → output`).  
- **`terminal_agent.py`** – Advanced terminal-based AI Agent with tool integrations:  
  - Generate complete Python or Web (HTML/CSS/JS) projects.  
  - Run system commands directly from prompts.  
  - Serve static HTML projects via a local server.  
  - Git automation (add, commit, push).  
  - Build mini-games like **Snake 🐍** and **Tic Tac Toe ❌⭕**.  

---

## 🚀 Key Features  

- **Prompt Engineering in Practice** – System prompts designed for behavior control.  
- **Reasoning Simulation** – Implements step-wise “chain-of-thought” reasoning.  
- **Autonomous Development Workflows** – AI that codes, executes, and deploys projects.  
- **Custom Tooling** – File handling, Git operations, project creation, and orchestration.  

---

## 🛠️ Tech Stack  

- **Languages:** Python  
- **SDKs:** OpenAI SDK, Gemini 1.5 Flash API  
- **Libraries:** `dotenv`, `requests`, `subprocess`, `json`, `os`, `webbrowser`  
- **Concepts:** Prompt Engineering, Chain-of-Thought, Tool-Augmented Agents, RAG (planned)  

---

## ⚡ Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/tauqueeralam42/gen-ai.git
cd gen-ai
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables
Create a .env file in the root directory:
```
GEMINI_API_KEY=your_api_key_here
```
### 4️⃣ Run Examples
# Basic chat examples
```
python chat_1.py
python chat_2.py
python chat_3.py
```
# Terminal AI Agent
``` 
python terminal_agent.py
```

## 🎯 Learning Outcomes  

- Hands-on experience with **OpenAI SDK** and **Gemini API**.  
- Building **domain-specific assistants** with controlled responses.  
- Implementing **step-by-step reasoning pipelines**.  
- Designing a **terminal AI agent** capable of coding, executing, and pushing projects to GitHub.  
- Exploring how **AI can act as a teammate** in software development workflows.  

---

## 📌 Future Enhancements  

- Integrate **RAG (Retrieval-Augmented Generation)** for external knowledge support.  
- Add **memory-based conversation tracking**.  
- Extend the agent with **API integrations and database operations**.  


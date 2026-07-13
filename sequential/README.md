
# 📰 AI News Research & Article Generator using CrewAI

A multi-agent AI application built with **CrewAI** that researches the latest trends on a given topic and generates a well-structured article using collaborative AI agents.

The project follows a **Sequential Process**, where each agent performs a dedicated task in order. The first agent researches the topic using web search, and the second agent uses that research to generate a comprehensive article.

---

# Features

- Multi-Agent AI Workflow
- Sequential Task Execution
- Web Search Integration using Serper API
- OpenAI GPT-4o-mini Integration
- Agent Memory
- Task Output Chaining
- Markdown Report Generation
- Modular Project Structure

---

# Workflow

```
                User Query
                     │
                     ▼
          Senior Researcher Agent
                     │
     Searches the latest information
                     │
                     ▼
         Research Report Generated
                     │
                     ▼
       News Retriever/Writer Agent
                     │
     Uses research to write article
                     │
                     ▼
            Markdown Output File
```

---

# Project Structure

```
project/
│
├── agents.py
├── tasks.py
├── tools.py
├── crew.py
├── solution.md
├── .env
├── requirements.txt
└── README.md
```

---

# Agents

## 1. Senior Researcher

### Responsibilities

- Research the given topic
- Identify latest trends
- Analyze market opportunities
- Identify advantages and disadvantages
- Collect reliable information using web search

---

## 2. News Retriever / Writer

### Responsibilities

- Read the research produced by the first agent
- Organize the information
- Generate an easy-to-understand article
- Save the final article as a Markdown file

---

# Tasks

## Research Task

The Senior Researcher:

- Searches the web
- Finds the latest developments
- Identifies trends
- Produces a research report

---

## Article Writing Task

The News Retriever Agent:

- Reads the research output
- Writes a detailed article
- Formats it in Markdown
- Saves it as:

```
solution.md
```

---

# Technologies Used

- Python
- CrewAI
- OpenAI GPT-4o-mini
- Serper API
- CrewAI Tools
- python-dotenv

---

# Installation

## Clone the Repository

```bash
git clone <repository-url>
cd project
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

---

# Running the Project

```bash
python crew.py
```

---

# Example Input

```text
Machine learning vs deep learning
```

---

# Example Workflow

```
User Query
      │
      ▼
Senior Researcher
      │
      ├── Search the web
      ├── Analyze latest trends
      ├── Identify opportunities
      └── Generate research
              │
              ▼
News Retriever Agent
      │
      ├── Read research
      ├── Organize findings
      ├── Write article
      └── Save as solution.md
```

---

# Crew Configuration

```python
crew = Crew(
    agents=[
        news_researcher,
        news_retriever_agent
    ],
    tasks=[
        get_research_task(),
        get_retriever_task()
    ],
    process=Process.sequential
)
```

---

# Tool Used

## SerperDevTool

The agents use **SerperDevTool** to perform internet searches and retrieve the latest information related to the user's query.

---

# Agent Memory

Both agents have memory enabled.

```python
memory=True
```

This allows them to retain relevant context throughout task execution.

---

# Output

The generated article is automatically saved as:

```
solution.md
```

The article includes:

- Topic overview
- Latest developments
- Industry impact
- Opportunities
- Challenges
- Future outlook

---

# Sample Execution

Input:

```
Machine learning vs deep learning
```

Output:

```
Research Report
        │
        ▼
Article Generated
        │
        ▼
solution.md
```

---

# Learning Outcomes

This project demonstrates:

- CrewAI Multi-Agent Systems
- Sequential Process
- Agent Collaboration
- Task Chaining
- Tool Calling
- Web Search Integration
- OpenAI LLM Integration
- Prompt Engineering
- Agent Memory
- Modular Project Design

---

# Future Enhancements

- Support multiple search tools
- Generate PDF reports
- Add citation and reference support
- Summarize articles automatically
- Support multiple LLM providers
- Add Streamlit or Chainlit interface
- Export articles to DOCX and PDF
- Schedule periodic news generation

---

# License

This project is intended for learning, experimentation, and educational purposes.
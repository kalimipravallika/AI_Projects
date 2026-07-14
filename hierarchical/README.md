# 🏠 Kitchen Support Multi-Agent System using CrewAI

A multi-agent AI system built using **CrewAI** that intelligently manages and resolves kitchen-related issues by delegating tasks to specialized agents.

The system uses a **Hierarchical Process**, where a **Kitchen Support Manager** analyzes the user's issue, delegates it to the appropriate specialist, performs web searches for relevant resources, and provides a comprehensive response.

---

# Features

- Multi-Agent Architecture using CrewAI
- Hierarchical Agent Delegation
- Specialized Kitchen Support Agents
- Web Search using Serper API
- Website Search Tool Integration
- OpenAI GPT-4o-mini Integration
- Agent Memory
- CrewAI Tracing Support
- Verbose Execution Logs

---

# Architecture

```
                    User Query
                         │
                         ▼
          Kitchen Support Manager (Manager Agent)
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 Cupboard Agent    Plumbing Agent    Electrical Agent
        │                │                │
        └────────────────┼────────────────┘
                         │
                Web Search Tools
          (Serper + Website Search)
                         │
                         ▼
                 Final Consolidated Report
```

---

# Agents

## 1. Kitchen Support Manager

## Responsibilities

- Analyze the reported issue
- Identify the appropriate specialist
- Delegate work
- Gather web resources
- Prepare the final response

---

## 2. Cupboard Specialist

Handles problems related to:

- Cupboard doors
- Hinges
- Shelves
- Handles
- Structural alignment

---

## 3. Water Tap Specialist

Handle:

- Water leakage
- Pipe issues
- Water pressure
- Tap maintenance

---

## 4. Electrical Appliance Specialist

Handle:

- Kitchen electrical sockets
- Lighting
- Appliances
- Wiring
- Electrical safety

---

# Technologies Used

- Python
- CrewAI
- OpenAI GPT-4o-mini
- Serper API
- CrewAI Tools
- python-dotenv

---

# Project Structure

```
KitchenSupport/
│
├── agenttask.py
├── .env
├── requirements.txt
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone <repository-url>
cd KitchenSupport
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

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
python agenttask.py
```

---

# Example Input

```text
In my kitchen, the cupboard door is misaligned and the water tap is leaking. I also have a problem with the electrical socket near the sink.
```

---

# Example Workflow

```
User
 │
 ▼
Kitchen Support Manager
 │
 ├── Detect cupboard issue
 │
 ├── Detect plumbing issue
 │
 ├── Detect electrical issue
 │
 ├── Search internet for repair resources
 │
 └── Generate final response
```

---

# Crew Configuration

```python
Crew(
    agents=[
        carpentry_specialist,
        plumbing_specialist,
        electrical_specialist
    ],
    tasks=[kitchen_issue_task],
    process=Process.hierarchical,
    manager_agent=manager,
    tracing=True,
    verbose=True
)
```

---

# Tools Used

## SerperDevTool

Used for:

- Internet search
- Troubleshooting resources
- Repair guides

---

## WebsiteSearchTool

Used for:

- Searching website content
- Retrieving additional information
- Supporting responses

---

# Agent Memory

All agents have memory enabled.

```python
memory=True
```

This allows agents to retain relevant context during execution.

---

# Tracing

Tracing is enabled.

```python
tracing=True
```

This allows you to visualize:

- Agent execution
- Task flow
- Tool calls
- LLM prompts
- Delegation
- Execution time
- Errors

After execution, CrewAI generates a trace link that can be viewed in the CrewAI dashboard.

---

# Sample Output

```
Assessment:
The kitchen has three reported issues:
- Misaligned cupboard door
- Leaking water tap
- Faulty electrical socket

Assigned Specialists:
- Cupboard Specialist
- Water Tap Specialist
- Electrical Appliance Specialist

Relevant Resources:
- Repair guides
- Troubleshooting articles
- Safety recommendations

Final Report:
A consolidated report containing the diagnosis, recommended repairs, and useful web resources.
```

---

# Future Improvements

- Image-based issue detection
- Voice input support
- PDF repair report generation
- Cost estimation for repairs
- Appointment scheduling
- Email notifications
- Integration with real maintenance services
- Multi-language support

---

# Learning Outcomes

This project demonstrates:

- CrewAI Multi-Agent Systems
- Hierarchical Process
- Agent Delegation
- Tool Calling
- OpenAI LLM Integration
- Prompt Engineering
- Memory Management
- AI Workflow Orchestration
- Agent Collaboration

---

# License

This project is developed for learning and educational purposes.
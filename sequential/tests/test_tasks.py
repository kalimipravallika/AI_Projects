from tasks import get_research_task, get_retriever_task

def test_research_task():
    task = get_research_task()

    assert "Identify the next big trend" in task.description
    assert task.agent.role == "Senior Researcher"

def test_retriever_task():
    task = get_retriever_task()

    assert "Compose an insightful article" in task.description
    assert task.output_file == "solution.md"
    assert task.async_execution is False
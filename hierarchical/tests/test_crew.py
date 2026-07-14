from agenttask import crew
from crewai import Process


def test_crew_created():
    assert crew is not None


def test_agents_count():
    assert len(crew.agents) == 3


def test_tasks_count():
    assert len(crew.tasks) == 1


def test_process():
    assert crew.process == Process.hierarchical


def test_manager():
    assert crew.manager_agent.role == "Kitchen Support Manager"
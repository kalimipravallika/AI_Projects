from crew import crew
from crewai import Process

def test_crew():
    assert len(crew.agents) == 2
    assert len(crew.tasks) == 2
    assert crew.process == Process.sequential
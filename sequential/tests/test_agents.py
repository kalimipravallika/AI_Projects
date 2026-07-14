from agents import news_researcher, news_retriever_agent

def test_news_researcher():
    assert news_researcher.role == "Senior Researcher"
    assert news_researcher.allow_delegation is True
    assert news_researcher.memory is not None

def test_news_retriever():
    assert "Retrieve relevant information" in news_retriever_agent.role
    assert news_retriever_agent.allow_delegation is False
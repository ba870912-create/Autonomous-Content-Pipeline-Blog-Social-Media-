from crewai import Agent, LLM
from crewai_tools import SerperDevTool

def create_researcher():
    llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0.1)
    return Agent(
        role="Research Agent",
        goal="Find trending insights and key data points about the topic.",
        backstory="You are an expert researcher who finds accurate information fast.",
        llm=llm,
        tools=[SerperDevTool()],
        verbose=True,
        allow_delegation=False,
        max_iter=2
    )
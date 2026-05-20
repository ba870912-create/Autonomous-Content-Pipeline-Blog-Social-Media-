from crewai import Agent, LLM

def create_strategist():
    llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0.7)
    return Agent(
        role="Content Strategist",
        goal="Create a clear content outline with key angles for the given topic.",
        backstory="You are a senior content strategist who plans viral content.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=2
    )
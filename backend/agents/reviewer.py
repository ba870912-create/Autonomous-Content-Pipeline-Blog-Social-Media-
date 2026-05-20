from crewai import Agent, LLM

def create_reviewer():
    llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0.1)
    return Agent(
        role="Quality Reviewer",
        goal="Review the blog and social posts for tone, accuracy, and quality.",
        backstory="You are a strict editor who ensures content meets high standards.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=2
    )
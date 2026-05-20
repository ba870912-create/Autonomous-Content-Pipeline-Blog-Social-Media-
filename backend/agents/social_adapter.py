from crewai import Agent, LLM

def create_social_adapter():
    llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0.8)
    return Agent(
        role="Social Media Adapter",
        goal="Transform the blog post into Twitter, LinkedIn, and Instagram captions with hashtags.",
        backstory="You are a social media expert who writes platform-specific content.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=2
    )
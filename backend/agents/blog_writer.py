from crewai import Agent, LLM

def create_blog_writer():
    llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0.7)
    return Agent(
        role="Blog Writer",
        goal="Write an SEO-optimized blog post based on the outline and research.",
        backstory="You are a professional tech blogger who writes engaging articles.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=2
    )
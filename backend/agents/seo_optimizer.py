from crewai import Agent, LLM

def create_seo_optimizer():
    llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0.1)  
    return Agent(
        role="SEO Optimizer",
        goal="Add meta title, meta description, focus keywords, and suggest internal links.",
        backstory="You are an SEO expert who optimizes content for search engines.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=2
    )
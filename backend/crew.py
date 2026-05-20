from crewai import Crew, Task, Process
from backend.agents.strategist import create_strategist
from backend.agents.researcher import create_researcher
from backend.agents.blog_writer import create_blog_writer
from backend.agents.social_adapter import create_social_adapter
from backend.agents.reviewer import create_reviewer
from backend.agents.seo_optimizer import create_seo_optimizer

def run_pipeline(topic: str, audience: str) -> dict:
    strategist = create_strategist()
    researcher = create_researcher()
    blog_writer = create_blog_writer()
    seo_optimizer = create_seo_optimizer()
    social_adapter = create_social_adapter()
    reviewer = create_reviewer()

    t1 = Task(
        description=f"Create a content outline for topic: '{topic}' targeting: '{audience}'.",
        expected_output="A structured outline with 5-7 key angles.",
        agent=strategist
    )
    t2 = Task(
        description=f"Research trending insights about: '{topic}'.",
        expected_output="5 key facts or statistics about the topic.",
        agent=researcher
    )
    t3 = Task(
        description="Write a 600-word SEO-optimized blog post using the outline and research.",
        expected_output="A complete blog post in markdown format.",
        agent=blog_writer,
        context=[t1, t2]
    )
    t_seo = Task(
        description="Add meta title, meta description, 5 focus keywords, and 3 suggested internal links for the blog post.",
        expected_output='{"meta_title": "...", "meta_description": "...", "keywords": [...], "internal_links": [...]}',
        agent=seo_optimizer,
        context=[t3]
    )
    t4 = Task(
        description="Create Twitter (280 chars), LinkedIn, and Instagram captions with hashtags.",
        expected_output="3 platform-specific posts with hashtags.",
        agent=social_adapter,
        context=[t3]
    )
    t5 = Task(
        description="Review the blog post and social captions for quality and accuracy.",
        expected_output="Final approved content or list of corrections.",
        agent=reviewer,
        context=[t3, t4]
    )

    crew = Crew(
        agents=[strategist, researcher, blog_writer, seo_optimizer, social_adapter, reviewer],
        tasks=[t1, t2, t3, t_seo, t4, t5],
        process=Process.sequential,
        verbose=False
    )

    crew.kickoff()

    return {
        "blog": str(t3.output),
        "seo": str(t_seo.output),
        "social": str(t4.output),
        "review": str(t5.output)
    }

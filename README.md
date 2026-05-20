# 📝 Autonomous Content Pipeline

A multi-agent AI system that generates SEO-optimized blog posts and social media content from a single topic.

## 🏗️ Architecture
Sequential multi-agent pipeline powered by CrewAI:
- **Content Strategist** — Creates content outline
- **Research Agent** — Gathers trending insights
- **Blog Writer** — Writes SEO-optimized article
- **SEO Optimizer** — Adds meta tags and keywords
- **Social Media Adapter** — Creates platform-specific posts
- **Quality Reviewer** — Validates content quality

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI
- **Frontend:** Streamlit
- **Agent Framework:** CrewAI
- **LLM:** Groq (llama-3.3-70b-versatile, llama-3.1-8b-instant)
- **Database:** PostgreSQL
- **Search:** Serper API

## ⚙️ Installation

```bash
git clone https://github.com/ba870912-create/Autonomous-Content-Pipeline-Blog-Social-Media-.git
cd Autonomous-Content-Pipeline-Blog-Social-Media-
pip install -r requirements.txt
```

## 🔑 Environment Variables
Create a `.env` file:
```env
GROQ_API_KEY=your_groq_key
SERPER_API_KEY=your_serper_key
DATABASE_URL=postgresql://postgres:password@localhost:5432/content_pipeline
```

## ▶️ Run
```bash
# Backend
uvicorn backend.main:app --reload

# Frontend
streamlit run frontend/app.py
```

## 📄 Sample Output
See [report.md](report.md)

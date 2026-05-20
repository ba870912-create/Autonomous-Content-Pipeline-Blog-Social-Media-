from fastapi import FastAPI
from pydantic import BaseModel
from backend.crew import run_pipeline
from backend.db.database import init_db
from backend.db.crud import save_content, get_all_posts
from dotenv import load_dotenv

load_dotenv()
init_db()  

app = FastAPI()

class PipelineRequest(BaseModel):
    topic: str
    audience: str

@app.post("/generate")
def generate(req: PipelineRequest):
    result = run_pipeline(req.topic, req.audience)
    save_content(
        topic=req.topic,
        audience=req.audience,
        blog=result["blog"],
        social=result["social"],
        seo=result["seo"],
        review=result["review"]
    )
    return result

@app.get("/history")
def history():
    posts = get_all_posts()
    return [
        {
            "id": p.id,
            "topic": p.topic,
            "created_at": str(p.created_at)
        }
        for p in posts
    ]
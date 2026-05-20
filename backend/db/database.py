from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class ContentPost(Base):
    __tablename__ = "content_posts"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String(255))
    audience = Column(String(255))
    blog = Column(Text)
    social = Column(Text)
    seo = Column(Text)
    review = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)
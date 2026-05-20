from backend.db.database import SessionLocal, ContentPost

def save_content(topic, audience, blog, social, seo, review):
    db = SessionLocal()
    try:
        post = ContentPost(
            topic=topic,
            audience=audience,
            blog=blog,
            social=social,
            seo=seo,
            review=review
        )
        db.add(post)
        db.commit()
        db.refresh(post)
        return post.id
    finally:
        db.close()

def get_all_posts():
    db = SessionLocal()
    try:
        return db.query(ContentPost).order_by(ContentPost.created_at.desc()).all()
    finally:
        db.close()
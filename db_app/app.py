"""
Simple SQL queries using SQLAlchemy and FastAPI
"""
from typing import List
from fastapi import FastAPI, HTTPException, Depends
from schema import PostGet, UserGet, FeedGet
from database import SessionLocal
from sqlalchemy.sql.functions import count
from sqlalchemy.orm import Session
from table_post import Post
from table_user import User
from table_feed import Feed
import uvicorn

app = FastAPI()

def get_db():
    with SessionLocal() as db:
        return db

@app.get("/user/{id}", response_model=UserGet)
def get_user_id(id: int, db: Session = Depends(get_db)):
    result = db.query(User).filter(User.id == id).one_or_none()
    if not result:
        raise HTTPException(404, f"404, user with id {id} not found")
    else:
        return result


@app.get("/post/{id}", response_model=PostGet)
def get_post_id(id: int, db: Session = Depends(get_db)):
    result = db.query(Post).filter(Post.id == id).one_or_none()
    if not result:
        raise HTTPException(404, f"404, post with id {id} not found")
    else:
        return result

@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(
        id: int,
        limit: int = 10,
        db: Session = Depends(get_db)
    ):
    result = db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all()
    return result


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(
        id: int,
        limit: int = 10,
        db: Session = Depends(get_db)
    ):
    result = db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()
    return result


@app.get("/post/recommendations/")
def get_recommended_feed(
        id: int,
        limit: int = 10,
        db: Session = Depends(get_db)
    ):
    result = db.query(Post)\
            .select_from(Feed)\
            .filter(Feed.action == 'like')\
            .join(Post)\
            .group_by(Post.id)\
            .order_by(count(Post.id).desc())\
            .limit(limit)\
            .all()

    return result

if __name__ == '__main__':
    print(__doc__)
    uvicorn.run("app:app", port=8895, reload=True)  # Запуск лок. сервера uvicorn с параметрами

import psycopg2
from typing import List
from fastapi import FastAPI, HTTPException, Depends
from loguru import logger
from schema import PostGet, UserGet, FeedGet
from database import SessionLocal
from sqlalchemy.orm import Session
from table_post import Post
from table_user import User
from table_feed import Feed

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

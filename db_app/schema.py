import psycopg2
import datetime
from pydantic import BaseModel

class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True

class UserGet(BaseModel):
    age: int = 0
    city: str
    country: str
    exp_group: int
    gender: int
    id: int
    os: str
    source: str

    class Config:
        orm_mode = True


class FeedGet(BaseModel):
    action: str
    post_id: int
    time: datetime.datetime
    user_id: int

    class Config:
        orm_mode = True


import psycopg2
import datetime
from pydantic import BaseModel

class PostGet(BaseModel):
    id: int = None
    text: str = ""
    topic: str = ""

    class Config:
        orm_mode = True

class UserGet(BaseModel):
    id: int = None
    gender: int = None
    age: int = None
    country: str = ""
    city: str = ""
    exp_group: int = None
    os: str = ""
    source: str = ""

    class Config:
        orm_mode = True


class FeedGet(BaseModel):
    user_id: int = None
    post_id: int = None
    action: str = ""
    time: datetime.datetime = None

    class Config:
        orm_mode = True

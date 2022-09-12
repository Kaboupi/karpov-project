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
    age: int = None
    city: str = ""
    country: str = ""
    exp_group: int = None
    gender: int = None
    id: int = None
    os: str = ""
    source: str = ""

    class Config:
        orm_mode = True


class FeedGet(BaseModel):
    action: str
    post_id: int
    time: datetime.datetime
    user_id: int

    class Config:
        orm_mode = True


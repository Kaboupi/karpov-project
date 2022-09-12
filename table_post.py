from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    gender = Column(Integer)
    age = Column(Integer)
    country = Column(String)
    city = Column(String)
    exp_group = Column(Integer)
    os = Column(String)
    source = Column(String)


if __name__ == '__main__':
    session = SessionLocal()
    li = []
    for post in (
        session.query(Post)
        .filter(Post.topic == "business")
        .order_by(Post.id.desc())
        .limit(10)
        .all()
    ):
        li.append(post.id)
    print(li)

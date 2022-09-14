from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from table_post import Post
from table_user import User

class Feed(Base):
    __tablename__ = 'feed_action'
    user_id = Column(
        Integer,
        ForeignKey(User.id),
        primary_key=True
    )
    post_id = Column(
        Integer,
        ForeignKey(Post.id)
    )
    action = Column(String)
    time = Column(DateTime)
    user = relationship(User)
    post = relationship(Post)


if __name__ == '__main__':
    session = SessionLocal()
    li = []
    for feed in (
        session.query(Feed)
        .filter(Feed.user_id == 1203)
        .order_by(Feed.post_id.desc())
        .limit(10)
        .all()
    ):
        li.append((feed.user_id, feed.post_id, feed.action, feed.time))
    print(li)
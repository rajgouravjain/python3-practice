from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.pool import  QueuePool
from concurrent.futures import ThreadPoolExecutor

import threading

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)


    def __repr__(self):
        return "<User(name='%s', age='%d')>" % (self.name, self.age)

engine = create_engine('mysql://rjain:pass@123@localhost:3306/learning', poolclass= QueuePool, pool_size = 2, max_overflow=0, pool_recycle=3600, echo=True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def worker():
    thread_session = Session()
    print(thread_session.query(User).filter_by(id=1).first())
    thread_session.commit()
    Session.remove()

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(worker)
    executor.submit(worker)
    executor.submit(worker)
    executor.submit(worker)
    executor.submit(worker)
    executor.submit(worker)


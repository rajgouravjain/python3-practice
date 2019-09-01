from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

session_factory = sessionmaker(bind=some_engine)
Session = scoped_session(session_factory)

def thread():
    thread_session = Session()
    # do my staff
    Session.remove()
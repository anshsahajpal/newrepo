from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.engine import create_engine
import traceback


db_file = "sqlite:///taskdb.sqlite"
Base = declarative_base()
engine = create_engine(db_file,connect_args={'check_same_thread':False},)

def get_db()->Session:
    session = Session(bind=engine,autoflush=False, autocommit=False)
    try:
        yield session
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        session.close()

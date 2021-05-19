from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os 

URL_MYSQL = os.getenv('URL_MYSQL')

engine = create_engine(URL_MYSQL, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

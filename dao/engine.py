from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

# sudo grep 'temporary password' /var/log/mysqld.log
# root@localhost: JxlA&T1M_264
# T00r@2021

URL_MYSQL = 'mysql+pymysql://root:T00r@2021@localhost/legislativo'

engine = create_engine(URL_MYSQL, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()
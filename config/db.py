# from sqlalchemy import create_engine, MetaData
# connection_str = "mysql+pymysql://arkademi:O26KnMOZFwp0L80P@baru-27oct-prod-rds.cn2z8bw9bvxv.ap-southeast-1.rds.amazonaws.com/arkademi"
# engine=create_engine(connection_str)
# meta=MetaData()
# con=engine.connect()

# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://arkademi:O26KnMOZFwp0L80P@baru-27oct-prod-rds.cn2z8bw9bvxv.ap-southeast-1.rds.amazonaws.com/arkademi"

db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

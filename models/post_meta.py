from config.db import Base
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Text, DateTime

class PostMeta(Base):
    __tablename__ = "sx5p1B_postmeta"
    meta_id = Column(Integer, primary_key=True)
    post_id = Column(Integer)
    meta_key=Column(String)
    meta_value=Column(String)

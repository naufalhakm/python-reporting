from config.db import Base
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Text, DateTime

class Kuesioner(Base):
    __tablename__ = "sx5p1B_kuesioner"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    category = Column(String)
    pertanyaan = Column(String)
    aktif = Column(Integer)
    index = Column(Integer)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
from models.BaseModel import EntityMeta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Text, DateTime

class Jawaban(EntityMeta):
    __tablename__ = "sx5p1B_jawaban"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    course_id = Column(Integer)
    pertanyaan_id=Column(Integer)
    jawaban=Column(String)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
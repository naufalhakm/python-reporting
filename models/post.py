from models.BaseModel import EntityMeta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Text, DateTime

class Post(EntityMeta):
    __tablename__ = "sx5p1B_posts"
    ID = Column(Integer, primary_key=True)
    post_author = Column(Integer)
    post_date = Column(DateTime())
    post_date_gmt = Column(DateTime())
    post_content=Column(Text)
    post_title=Column(String)
    post_excerpt=Column(String)
    post_status=Column(String)
    comment_status=Column(String)
    ping_status=Column(String)
    post_password=Column(String)
    post_name=Column(String)
    to_ping=Column(Text)
    pinged=Column(Text)
    post_modified = Column(DateTime())
    post_modified_gmt = Column(DateTime())
    post_content_filtered = Column(Text)
    post_parent = Column(Integer)
    guid=Column(String)
    menu_order = Column(Integer)
    post_type=Column(String)
    post_mime_type=Column(String)
    comment_count = Column(Integer)

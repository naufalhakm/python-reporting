from config.db import Base
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Text, DateTime

class Users(Base):
    __tablename__ = "sx5p1B_users"
    ID = Column(Integer, primary_key=True)
    user_login = Column(String)
    user_pass = Column(String)
    user_nicename = Column(String)
    user_url = Column(String)
    user_registered = Column(DateTime())
    user_activation_key=Column(String)
    user_status = Column(Integer)
    display_name=Column(String)
    role=Column(String)
    api_token=Column(String)
    user_email_new=Column(String)
    user_email_new_verify_token=Column(String)
    forgot_password_token=Column(String)
    forgot_password_token_expiration=Column(String)
    user_email_new_verify_token_expiration=Column(String)
    fcm_token=Column(String)
    device=Column(String)
    organization_id = Column(Integer)

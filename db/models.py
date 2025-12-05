from sqlalchemy import Column, Integer,String, Boolean, Float
from db.database import Base

class DbBlog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    
    

class DbUser(Base):
    __tablename__ = "users"
    
    id  = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)

    
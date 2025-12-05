from pydantic import BaseModel
from typing import Optional

# Schema for incoming data (Request Body)
class BlogCreate(BaseModel):
    title:str
    content:str
    
class BlogUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None   
    

# Schema for outgoing data (Response Body)
class BlogDisplay(BaseModel):
    id:int
    title:str
    content:str
    
    class Config:
        from_attributes = True
    
from fastapi import APIRouter, Depends, HTTPException
from schema import BlogCreate, BlogDisplay, BlogUpdate
from db.database import get_db
from sqlalchemy.orm import Session
from db.models import DbBlog
from typing import List

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

#POST
@router.post("", response_model=BlogDisplay)
def create_blog(blog:BlogCreate, db:Session = Depends(get_db)):
    
    new_blog = DbBlog(
        title = blog.title,
        content = blog.content
        
    )
    db.add(new_blog) # Add in Db
    db.commit()  # Permanantly added in Db
    db.refresh(new_blog) #Refresh to get the new created blog
    return new_blog
    
#GET
@router.get("",response_model=List[BlogDisplay])
def get_all_blogs( db:Session = Depends(get_db)):
    blogs = db.query(DbBlog).all()
    return blogs

#GET Single Blog
@router.get("/{id}")
def get_blog(id:int, db:Session = Depends(get_db)):
    blog = db.query(DbBlog).filter(DbBlog.id == id).first()
    return blog

#PUT
@router.put("/{id}")
def update_blog(id:int, blog: BlogCreate, db:Session = Depends(get_db)):
    existing_blog = db.query(DbBlog).filter(DbBlog.id == id).first()
    
    existing_blog.title = blog.title
    existing_blog.content = blog.content
    db.commit()
    db.refresh(existing_blog)
    return existing_blog
    
    

#PATCH
# Partially update blog (PATCH)
@router.patch("/{id}", response_model=BlogDisplay)
def patch_blog(id: int, blog_update: BlogUpdate, db: Session = Depends(get_db)):
    blog_to_update = db.query(DbBlog).filter(DbBlog.id == id).first()

    if blog_update.title is not None:
        blog_to_update.title = blog_update.title
    if blog_update.content is not None:
        blog_to_update.content = blog_update.content

    db.commit()
    db.refresh(blog_to_update)
    return blog_to_update

#DELETE
@router.delete("/{id}")
def delete_blog(id:int,db: Session = Depends(get_db)):
    blog_to_delete = db.query(DbBlog).filter(DbBlog.id == id).first()
    
    if not blog_to_delete:
        raise HTTPException(status_code=404, detail="Blog Not Found")
    
    db.delete(blog_to_delete)
    db.commit()
    return {"message": "Blog deleted successfully"}
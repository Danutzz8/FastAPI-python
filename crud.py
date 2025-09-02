# crud.py
from sqlalchemy.orm import Session
import models, schemas, auth

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not auth.verify_password(password, user.hashed_password):
        return None
    return user


# Posts
def create_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(title=post.title, content=post.content, owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session):
    return db.query(models.Post).all()


# Comments
def create_comment(db: Session, comment: schemas.CommentCreate, post_id: int, user_id: int):
    db_comment = models.Comment(text=comment.text, post_id=post_id, author_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments(db: Session, post_id: int):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()

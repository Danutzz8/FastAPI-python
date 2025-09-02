# app.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import models, schemas, crud, auth
from database import engine, SessionLocal

# create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API with JWT Auth")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

# --------- AUTH ---------
@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)


@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


# --------- USERS ---------
@app.get("/users/me", response_model=schemas.UserOut)
def get_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user


# --------- POSTS ---------
@app.post("/posts", response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_post(db, post, current_user.id)


@app.get("/posts", response_model=list[schemas.PostOut])
def list_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)


# --------- COMMENTS ---------
@app.post("/posts/{post_id}/comments", response_model=schemas.CommentOut)
def create_comment(post_id: int,
                   comment: schemas.CommentCreate,
                   db: Session = Depends(get_db),
                   current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_comment(db, comment, post_id, current_user.id)


@app.get("/posts/{post_id}/comments", response_model=list[schemas.CommentOut])
def get_comments(post_id: int, db: Session = Depends(get_db)):
    return crud.get_comments(db, post_id)

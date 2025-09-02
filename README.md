# FastAPI Blog API with JWT Authentication..........

A simple blog API built with **FastAPI**, **SQLAlchemy**, and **JWT authentication**.  
It supports user registration, login, creating posts, and adding comments.  

---

## Features

- User registration (`POST /register`)  
- User login with JWT (`POST /login`)  
- JWT-protected routes  
- CRUD for posts and comments:
  - Create posts (`POST /posts`)
  - List posts (`GET /posts`)
  - Add comments (`POST /posts/{post_id}/comments`)
  - Get comments (`GET /posts/{post_id}/comments`)  
- Automatic API documentation with Swagger UI (`/docs`) and ReDoc (`/redoc`)  

---

## Tech Stack

- Python 3.11+  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [SQLite](https://www.sqlite.org/) (default, can be replaced with PostgreSQL/MySQL)  
- [JWT](https://jwt.io/) for authentication  

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/fastapi-blog-api.git
cd fastapi-blog-api
```
2. Create a virtual environment and activate it:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
   ```
   pip install -r requirements.txt
```
pip install python-multipart email-validator
```

Running the app
```
pip install python-multipart email-validator
```

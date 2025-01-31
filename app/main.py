from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .db import create_db_and_tables
from .routers import auth, belvo, users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=(settings.allowed_origins.split(",")),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(belvo.router)
app.include_router(users.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

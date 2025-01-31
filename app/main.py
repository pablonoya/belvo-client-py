from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routers import belvo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=(settings.allowed_origins.split(",")),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(belvo.router)

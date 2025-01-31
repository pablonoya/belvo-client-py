from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    allowed_origins: str = "http://localhost:3000"
    belvo_base_url: str = "https://sandbox.belvo.com/api"
    belvo_username: str
    belvo_password: str

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()

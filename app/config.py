from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    allowed_origins: str = "http://localhost:3000"
    belvo_base_url: str = "https://sandbox.belvo.com/api"
    belvo_username: str
    belvo_password: str


settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "TaskFlow API"
    database_url: str = "sqlite:///./taskflow.db"
    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
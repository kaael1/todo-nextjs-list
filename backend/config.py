from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_HOST: str = "localhost"
    DATABASE_NAME: str = "mydatabase"
    DATABASE_USER: str = "user12"
    DATABASE_PASSWORD: str = "pass12"
    DATABASE_PORT: int = 5432
    app_name: str = "Full Stack To Do App"

    class Config:
        env_file = ".env"
        extra = "ignore"

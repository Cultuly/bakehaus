# Settings configuration dependencies
from pydantic_settings import BaseSettings, SettingsConfigDict
# Context dependencies
from core.dependencies import BASE_DIR


# Settings container
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env",
        env_file_encoding="utf-8"
    )

    # Database section
    db_host: str = "localhost"
    db_name: str = "bakehaus"
    db_user: str = "admin"
    db_password: str = "password"
    db_port: int = 5432


# Settings instance (loading from .env file)
settings = Settings()
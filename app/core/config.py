from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Smart Mobility Backend"
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./smart_mobility.db"
    sqlite_foreign_keys: bool = True
    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:5173"]
    jwt_secret: str = "change-me-in-development"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()

from dataclasses import dataclass
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    app_name: str = "MyFastAPIApp"
    debug: bool = False
    host: str = "127.0.0.1"
    port: int = 8000
    database_url: str = "sqlite:///./test.db"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# ENV_STATE 값에 따라 env_file 동적으로 변경
env_state = os.getenv("ENV_STATE", "dev")

if env_state == "prod":
    Settings.model_config["env_file"] = ".env.prod"
elif env_state == "test":
    Settings.model_config["env_file"] = ".env.test"
else:
    Settings.model_config["env_file"] = ".env.dev"

settings = Settings()
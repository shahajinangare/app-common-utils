# app/core/config.py
from functools import lru_cache
from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Any
from pathlib import Path
import os

def get_env_file():
    """Load common .env + environment‑specific .env file"""
    # Get environment from os.environ first (fast, no file read)
    # Print(os.getenv("ENVIRONMENT"))
    env_name =os.getenv("ENVIRONMENT", default="development")
    # Build env file path
    env_file = Path.cwd() / f".env.{env_name}"
    return env_file

class AppSettings(BaseSettings):
    name: str = "auth-service"
    environment: str = "development"
    debug: bool = True
    version: str = "0.1.0"
    log_level: str = "INFO"  # DEBUG, INFO, WARNING, ERROR

    model_config = SettingsConfigDict(env_prefix="APP_", env_file=str(get_env_file()), extra="ignore")

class SecuritySettings(BaseSettings):
    secret_key: str = "secret_key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    cors_allow_origins: list[str] = ["*"]
    
    model_config = SettingsConfigDict(env_prefix="SEC_", env_file=str(get_env_file()), extra="ignore")

class DatabaseSettings(BaseSettings):
    mysql_user: str
    mysql_pwd: str
    mysql_host: str
    mysql_port: str = 3306
    mysql_database_name: str
    pool_size: int = 10

    model_config = SettingsConfigDict(env_prefix="DB_",env_file=str(get_env_file()),   extra="ignore")

class ThirdPartySettings(BaseSettings):
    sentry_dsn: str | None = None
    redis_url: str | None = None

    model_config = SettingsConfigDict(env_prefix="TP_",env_file=str(get_env_file()), extra="ignore")

class ApiSettings(BaseSettings):
    pg_x_key: str | None = None
    ekyc_x_key: str | None = None
    sms_x_key: str | None = None       
    email_x_key: str | None = None
    esign_x_key: str | None = None
    base_url: str | None = None
    token_base_url: str | None = None
    token_username: str | None = None
    token_pwd: str | None = None
    
    model_config = SettingsConfigDict(env_prefix="API_",env_file=str(get_env_file()), extra="ignore")

class EmailSettings(BaseSettings):
    host:str | None = None
    port:str | None = None
    username:str | None = None
    password:str | None = None

    model_config = SettingsConfigDict(env_prefix="EMAIL_",env_file=str(get_env_file()), extra="ignore")

class SmsSettings(BaseSettings):
    username:str | None = None
    password:str | None = None
    senderid:str | None = None

    model_config = SettingsConfigDict(env_prefix="SMS_",env_file=str(get_env_file()), extra="ignore")


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    security: SecuritySettings = SecuritySettings()
    db: DatabaseSettings = DatabaseSettings()
    third_party: ThirdPartySettings = ThirdPartySettings()
    api:ApiSettings=ApiSettings()
    email:EmailSettings=EmailSettings()
    sms:SmsSettings=SmsSettings()

@lru_cache
def get_settings()-> Settings:
    #return Settings(_env_file=str(get_env_file()))
    return Settings()
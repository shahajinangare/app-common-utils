from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import AsyncGenerator
import os
from dotenv import load_dotenv

from app_common_utils.core.config import get_settings

# Load config FIRST
settings = get_settings()

load_dotenv()

# Async MySQL URL: mysql+aiomysql://user:pass@host:port/db
DATABASE_URL = (
    f"mysql+aiomysql://{settings.db.mysql_user}:{settings.db.mysql_pwd}@"
    f"{settings.db.mysql_host}:{settings.db.mysql_port}/{settings.db.mysql_database_name}?"
    f"charset=utf8mb4"
)
# print(DATABASE_URL)
# Connection pooling for production
engine = create_async_engine(
    DATABASE_URL,
    echo=True,           # SQL logging
    pool_size=settings.db.pool_size,
    max_overflow=20,
    pool_pre_ping=True,  # Validate connections
    pool_recycle=3600    # Refresh idle connections every hour
)

AsyncSessionLocal = async_sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False,
    autoflush=False,    # Explicit control
    autocommit=False
)

Base = declarative_base()

# Import your models HERE 
from app_common_utils.models import user_model

# Create tables on startup (run once)
async def init_db():
    async with engine.begin() as conn:
        # Drop existing tables first (use with caution!)
        # await conn.run_sync(Base.metadata.drop_all)
        
        # Create all tables from models
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tables created successfully : {}".format(list(Base.metadata.tables.keys())))

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    session = AsyncSessionLocal()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
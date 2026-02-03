import asyncio
from sqlalchemy import select
from app_common_utils.db.base import engine, get_db  
from app_common_utils.models.user_model import User

async def get_users():
    async for db in get_db():
        result = await db.execute(select(User))
        users = result.scalars().all()
        for user in users:
            print(f"  ID: {user.id}, Name: {user.username}")  # Adjust fields

async def main():
    try:
        await get_users()
    finally:
        # CRITICAL: Dispose engine before loop closes
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())
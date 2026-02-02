from app.db.base import init_db, engine

class DatabaseLifespan:
    async def __aenter__(self):
        """Startup - runs when app starts"""
        print("🚀 Starting up...")
        await init_db()
        print("✅ Database tables ready")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Shutdown - runs when app stops"""
        print("🛑 Shutting down...")
        await engine.dispose()
        print("✅ Database connections closed")
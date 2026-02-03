# app/models/user.py
from sqlalchemy import DateTime, String, Integer, Column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.sql import func
from app_common_utils.db.base import Base
from datetime import datetime

class User(AsyncAttrs, Base):
    __tablename__ = "users"
   
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    fullname = Column(String(100), nullable=False)
    mobileno = Column(String(12), unique=True, index=True, nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(500), nullable=False)
    user_type = Column(String(20), nullable=False)
    is_active = Column(Integer, default=1)
    # ✅ Auto-set on create, MySQL TIMESTAMP
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),  # MySQL CURRENT_TIMESTAMP
        nullable=False
    )
    # ✅ Auto-update on changes
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
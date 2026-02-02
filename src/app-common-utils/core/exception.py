from enum import Enum
from fastapi import HTTPException, status

class ErrorCode(Enum):
    TOKEN = "TOKEN"
    USER_NOT_FOUND = "USER_NOT_FOUND" 
    INVALID_USERNAME_PASSWORD = "INVALID_USERNAME_PASSWORD"
    INVALID_USER = "INVALID_USER"
    REDIS_NOT_AVAILABLE = "REDIS_NOT_AVAILABLE"

class HTTP_EXCEPTION:
    TOKEN = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    USER_NOT_FOUND=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    INVALID_USERNAME_PASSWORD = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    ACCESS_DENIED=HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    
class REDIS_SERVER_EXCEPTION:
    REDIS_NOT_AVAILABLE=HTTPException(status_code=101,detail="⚠️ Redis server unavailable. Please contact to Administrator.")

class USER_EXCEPTION:
    INVALID_USER=HTTPException(status_code=201,detail="INVALID USER !!!")
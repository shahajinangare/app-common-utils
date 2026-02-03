from app_common_utils.core.config import get_settings

settings = get_settings()
print(settings.app.name)

from app_common_utils.core.constants import SMS_API_URL

print(SMS_API_URL.SERVICE_NAME)

from app_common_utils.core.exception import HTTP_EXCEPTION
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
import json

response =JSONResponse(status_code=HTTP_EXCEPTION.ACCESS_DENIED.status_code,content=HTTP_EXCEPTION.ACCESS_DENIED.detail)
print(response.body.decode('utf-8'))
print(response.status_code)
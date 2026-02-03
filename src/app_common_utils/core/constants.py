from enum import Enum
from typing import Final
from app_common_utils.core.config import get_settings

settings = get_settings()

class PHONEPE_API_URL(str, Enum):
    SERVICE_NAME ="payment-gateway-service"
    CREATE_PAYMENT_PAY= f"{settings.api.base_url}/{SERVICE_NAME}/v1/pp/pg/create/payments/pay"
    CREATE_CHECKOUT_PAY= f"{settings.api.base_url}/{SERVICE_NAME}/v1/pp/pg/create/checkout/pay"
    INITIATE_REFUND= f"{settings.api.base_url}/{SERVICE_NAME}/v1/pp/pg/initiate/refund"
    ORDER_STATUS= f"{settings.api.base_url}/{SERVICE_NAME}/v1/pp/pg/order/status"

class SMS_API_URL(str, Enum):
    SERVICE_NAME ="sms-service"
    SEND_SMS= f"{settings.api.base_url}/{SERVICE_NAME}/v1/sms/otp"s
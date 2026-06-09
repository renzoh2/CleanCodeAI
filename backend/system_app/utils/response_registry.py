from .app_codes import AppCodes
from dataclasses import dataclass

@dataclass(frozen=True)
class registry:
    label: str | None
    message: str

class ResponseRegistry:

    MESSAGE_REGISTRY: dict[AppCodes, registry] = {
        AppCodes.EMPTY_FIELDS: registry(label=None, message="Please complete all required fields."),
        AppCodes.MISSING_EMAIL: registry(label=None, message="Please enter your Email Address."),
        AppCodes.MISSING_PASSWORD: registry(label=None, message="Please enter your Password."),
        AppCodes.EMAIL_NOT_EXIST: registry(label=None, message="No account exists with the provided email."),
        AppCodes.INVALID_PASSWORD: registry(label=None, message="Incorrect password. Please try again."),
        AppCodes.LOGIN_FAILED: registry(label=None, message="Unable to log in. Please review your email and password."),
        AppCodes.LOGIN_ERROR: registry(label=None, message="Login unavailable. We are experiencing technical difficulties. Please try again later."),
        AppCodes.SYSTEM_ERROR: registry(label=None, message="Service temporarily unavailable. We are working to restore access as quickly as possible")
    }

    def get_registry(self, code: AppCodes):

        metadata = self.MESSAGE_REGISTRY.get(code)

        # Fallback safety default
        if not metadata:
            return { "message": None }
        
        return { "message": metadata.message }
    
    def to_response(self, code: AppCodes, status: bool, data: dict | None = None):

        #Get messge response
        if not status:
            data = self.get_registry(code=code)

        return {
            "status": status,
            "code": code,
            "data": data
        }
    
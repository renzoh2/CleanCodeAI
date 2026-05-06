from typing import Any
from pydantic import BaseModel, model_validator
from web_backend.system_app.enums import SystemEnums
class LoginAPI(BaseModel):
    email: str
    password: str

    @model_validator(mode="before")
    def validate_fields(cls, data: Any) -> Any:
        if "email" not in data:
            return SystemEnums.MISSING_EMAIL
        if "password" not in data:
            return SystemEnums.MISSING_PASSWORD
        return data
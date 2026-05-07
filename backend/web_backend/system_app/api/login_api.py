from typing import Any
from pydantic import BaseModel, model_validator
from web_backend.system_app.enums import SystemEnums
class LoginAPI(BaseModel):
    email: str | None
    password: str | None

    @model_validator(mode="before")
    def validate_fields(cls, data: Any) -> Any:
        if data["email"] == "" and data["password"] == "":
            raise ValueError(SystemEnums.EMPTY_FIELDS)
        if data["email"] is None and data["password"] is None:
            raise ValueError(SystemEnums.EMPTY_FIELDS)
        if "email" not in data:
            raise ValueError(SystemEnums.MISSING_EMAIL)
        if data["email"] == "":
            raise ValueError(SystemEnums.MISSING_EMAIL)
        if "password" not in data:
            raise ValueError(SystemEnums.MISSING_PASSWORD)
        if data["password"] == "":
            raise ValueError(SystemEnums.MISSING_PASSWORD)
        return data
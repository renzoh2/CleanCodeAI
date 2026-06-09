from typing import Any
from pydantic import BaseModel, model_validator
from ..utils import AppCodes
class LoginAPI(BaseModel):
    email: str | None
    password: str | None

    @model_validator(mode="before")
    def validate_fields(cls, data: Any) -> Any:
        if data["email"] == "" and data["password"] == "":
            raise ValueError(AppCodes.EMPTY_FIELDS)
        if data["email"] is None and data["password"] is None:
            raise ValueError(AppCodes.EMPTY_FIELDS)
        if "email" not in data:
            raise ValueError(AppCodes.MISSING_EMAIL)
        if data["email"] == "":
            raise ValueError(AppCodes.MISSING_EMAIL)
        if "password" not in data:
            raise ValueError(AppCodes.MISSING_PASSWORD)
        if data["password"] == "":
            raise ValueError(AppCodes.MISSING_PASSWORD)
        return data
import graphene

class SystemEnums(graphene.Enum):
    
    #Login Codes
    LOGIN_SUCCESS = "LOGIN_SUCCESS"
    EMAIL_NOT_EXIST = "EMAIL_NOT_EXIST"
    MISSING_EMAIL = "MISSING_EMAIL"
    MISSING_PASSWORD = "MISSING_PASSWORD"
    INVALID_PASSWORD = "INVALID_PASSWORD"
    LOGIN_FAILED = "LOGIN_FAILED"
    LOGIN_ERROR = "LOGIN_ERROR"

    #System Codes
    SYSTEM_ERROR = "SYSTEM_ERROR"

    def __str__(self):
        return self.value

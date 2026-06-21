from apps.authentication.models import UserAccount
from apps.authentication.api.login_api import LoginAPI
from django.contrib.auth.hashers import make_password, check_password
from django.forms.models import model_to_dict
from apps.authentication.utils.functions import dict_format
#Utilities
from apps.authentication.utils import AppCodes, ResponseRegistry

class AuthenticationService:

    def __init__(self):
        self.response_registry = ResponseRegistry()

    #Logging In
    def login(self, request: LoginAPI) -> dict:

        try:
            #Email Validation
            user = UserAccount.objects.filter(email=request.email).first()
           
            if not user:
                return self.response_registry.to_response(
                    code=AppCodes.EMAIL_NOT_EXIST, 
                    status=False
                )
            
            password_status = check_password(
                 password=request.password,
                 encoded=user.password_hashed
            )

            if not password_status:
                return self.response_registry.to_response(
                    code=AppCodes.INVALID_PASSWORD,
                    status=False
            )
            
            return self.response_registry.to_response(
                code=AppCodes.LOGIN_SUCCESS,
                status=True,
                data=dict_format(
                    model_to_dict(user)
                )
            )
            
        except:
            return self.response_registry.to_response(
                code=AppCodes.LOGIN_FAILED,
                status=False
            )
        
    def getMessageFromCode():
        pass
       
    def generateHashed(password):
        return make_password(password)

from .models import User
from .api.login_api import LoginAPI
from django.contrib.auth.hashers import make_password, check_password
from .enums import SystemEnums

class SystemAppService:

    #Logging In
    def login(request: LoginAPI) -> dict:

        #Parsing Returning Data (Maybe will parse data)
        def return_login_data(status: str, data: User | None):
            return {
                "status": status,
                "data": data
            }

        try:
            #Email Validation
            user = User.objects.filter(email=request.email).first()

            if not user:
                return return_login_data(status=SystemEnums.EMAIL_NOT_EXIST, data=None)
            
            password_status = check_password(
                 password=request.password,
                 encoded=user.password_hashed
            )

            if not password_status:
                return return_login_data(status=SystemEnums.INVALID_PASSWORD, data=None)
           
            return return_login_data(status=SystemEnums.LOGIN_SUCCESS, data=user) #Return User
        except:
            return return_login_data(status=SystemEnums.LOGIN_FAILED, data=None)
        
    def getMessageFromCode():
        pass
       
    def generateHashed(password):
        return make_password(password)

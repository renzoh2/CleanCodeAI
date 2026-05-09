import graphene
from system_app.service import SystemAppService
from system_app.api.login_api import LoginAPI
from system_app.enums import SystemEnums
from system_app.graphql.model_types import UserTypes
from .base_mutation import BaseMutation
from pydantic import ValidationError

class LoginMutation(BaseMutation):
    class Arguments:
        email = graphene.String(required=False)
        password = graphene.String(required=False)

    user = graphene.Field(UserTypes)

    def mutate(root, info, email=None, password=None):
        print(info)
        try:
            service = SystemAppService.login(LoginAPI(email=email, password=password))
           
            if type(service) is not dict:
                return LoginMutation(code=service["status"], message=service["message"])
            
            return LoginMutation(user=service["data"], code=service["status"], message=service["message"])
        except ValidationError as e:
            code = str(e.errors()[0]["ctx"].get("error")) #Get Error Code from Pydantic Raise Value Error
            return LoginMutation(code=code,message="Invalid Data")
        except Exception as e:
            return LoginMutation(code=SystemEnums.SYSTEM_ERROR, message=e)

class DummyMutation(graphene.Mutation):
    ok = graphene.Boolean()

    def mutate(root, info):
        return DummyMutation(ok=True)
    
class GeneratePasswordHashedMutation(graphene.Mutation):
    class Arguments:
        password = graphene.String()

    hashed = graphene.String()

    def mutate(root, info, password):
        hashed = SystemAppService.generateHashed(password=password)
        return GeneratePasswordHashedMutation(hashed = hashed)
    
class SystemAppMutation(graphene.ObjectType):
    dummy = DummyMutation.Field()
    generate = GeneratePasswordHashedMutation.Field()
    login = LoginMutation.Field()
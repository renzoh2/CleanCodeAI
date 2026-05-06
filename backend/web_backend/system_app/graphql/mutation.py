import graphene
from web_backend.system_app.service import SystemAppService
from web_backend.system_app.api.login_api import LoginAPI
from web_backend.system_app.enums import SystemEnums
from web_backend.system_app.graphql.model_types import UserTypes
from .base_mutation import BaseMutation

class LoginMutation(BaseMutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserTypes)

    def mutate(root, info, email, password):
        try:
            service = SystemAppService.login(LoginAPI(email=email, password=password))
           
            if type(service) is not tuple:
                return LoginMutation(code=service, message="Login Failed")
            
            return LoginMutation(user=str(service[1]), code=service[0], message="Login Success")
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
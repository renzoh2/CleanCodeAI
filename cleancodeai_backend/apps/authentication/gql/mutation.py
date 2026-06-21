import graphene
from apps.authentication.service import AuthenticationService
from apps.authentication.api.login_api import LoginAPI
from apps.authentication.utils import AppCodes, ResponseRegistry
from apps.authentication.gql.model_types import UserAccountTypes
from pydantic import ValidationError
from graphene.types.generic import GenericScalar

class LoginMutation(graphene.Mutation):
    status = graphene.Boolean()
    code = graphene.String()
    data = GenericScalar()
    class Arguments:
        email = graphene.String(required=False)
        password = graphene.String(required=False)

    user = graphene.Field(UserAccountTypes)

    def mutate(root, info, email=None, password=None):
        registry = ResponseRegistry()
        auth_service = AuthenticationService()
        try:
      
            service = auth_service.login(LoginAPI(email=email, password=password))
   
            if type(service) is not dict:
                return LoginMutation(
                    **registry.to_response(
                        code=AppCodes.SYSTEM_ERROR,
                        status=False
                    )
                )
            
            return LoginMutation(**service)
        except ValidationError as e:
            code = str(e.errors()[0]["ctx"].get("error")) #Get Error Code from Pydantic Raise Value Error
            return LoginMutation(
                **registry.to_response(
                    code=code,
                    status=False
                )
            )
        except Exception as e:
            return LoginMutation(
                **registry.to_response(
                    code=AppCodes.SYSTEM_ERROR,
                    status=False,
                    data=e.__dict__
                )
            )

class DummyMutation(graphene.Mutation):
    ok = graphene.Boolean()

    def mutate(root, info):
        return DummyMutation(ok=True)
    
class GeneratePasswordHashedMutation(graphene.Mutation):
    class Arguments:
        password = graphene.String()

    hashed = graphene.String()

    def mutate(root, info, password):
        hashed = AuthenticationService.generateHashed(password=password)
        return GeneratePasswordHashedMutation(hashed = hashed)
    
class AuthenticationMutation(graphene.ObjectType):
    dummy = DummyMutation.Field()
    generate = GeneratePasswordHashedMutation.Field()
    login = LoginMutation.Field()
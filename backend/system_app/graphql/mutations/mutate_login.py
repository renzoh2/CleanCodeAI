import graphene
from ...service import SystemAppService
from ...api.login_api import LoginAPI
from ...utils import AppCodes, ResponseRegistry
from ...graphql.model_types import UserTypes
from pydantic import ValidationError
from graphene.types.generic import GenericScalar

class LoginMutation(graphene.Mutation):
    status = graphene.Boolean()
    code = graphene.String()
    data = GenericScalar()
    class Arguments:
        email = graphene.String(required=False)
        password = graphene.String(required=False)

    user = graphene.Field(UserTypes)

    def mutate(root, info, email=None, password=None):
        registry = ResponseRegistry()
        try:
            service = SystemAppService.login(LoginAPI(email=email, password=password))
            
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
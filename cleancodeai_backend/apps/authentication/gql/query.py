import graphene

from apps.authentication.models import (
    UserAccount
)

from apps.authentication.gql.model_types import (
    UserAccountTypes
)

#Query Resolvers
class AuthenticationQuery(graphene.ObjectType):
    all_users = graphene.List(UserAccountTypes)
    user = graphene.Field(UserAccountTypes, id=graphene.String())

    def resolve_all_users(root, info):
        return UserAccount.objects.all()
    
    def resolve_user(root, info, id):
        return UserAccount.objects.filter(id=id).get()
import graphene

from web_backend.system_app.models import (
    User,
    Profile
)

from .model_types import (
    UserTypes,
    ProfileTypes
)

#Query Resolvers
class SystemAppQuery(graphene.ObjectType):
    all_users = graphene.List(UserTypes)
    all_profile = graphene.List(ProfileTypes)
    profile = graphene.Field(ProfileTypes, id=graphene.String())
    all_profile_with_user_data = graphene.List(ProfileTypes)

    def resolve_all_users(root, info):
        return User.objects.all()
    
    def resolve_all_profile_with_user_data(root, info):
        return Profile.objects.prefetch_related("profiles__user_id").all()
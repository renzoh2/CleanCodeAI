import graphene
from graphene_django import DjangoObjectType

from web_backend.system_app.models import (
    User,
    Profile,
    UserProfile
)

class UserModel(DjangoObjectType):
    class Meta:
        model=User
        fields=("id","email","password","password_hashed","is_active","is_locked","created_at","updated_at")

class ProfileModel(DjangoObjectType):
    class Meta:
        model=Profile
        Fields=("id","last_name")

class UserProfileModel(DjangoObjectType):
    class Meta:
        model=UserProfile
        Fields=("id","profile_id","user_id")

class Query(graphene.ObjectType):
    all_users = graphene.List(UserModel)
    all_profile = graphene.List(ProfileModel)
    profile = graphene.Field(ProfileModel, id=graphene.String())
    all_profile_with_user_data = graphene.List(ProfileModel)

    def resolve_all_users(root, info):
        return User.objects.all()
    
    def resolve_all_profile_with_user_data(root, info):
        return Profile.objects.prefetch_related("profiles__user_id").all()
    
schema = graphene.Schema(query=Query)
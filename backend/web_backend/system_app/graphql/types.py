import graphene
from graphene_django import DjangoObjectType

from web_backend.system_app.models import (
    User,
    Profile,
    UserProfile
)

class UserTypes(DjangoObjectType):
    class Meta:
        model=User
        fields=("id","email","password","password_hashed","is_active","is_locked","created_at","updated_at")

class ProfileTypes(DjangoObjectType):
    class Meta:
        model=Profile
        Fields=("id","last_name")

class UserProfileTypes(DjangoObjectType):
    class Meta:
        model=UserProfile
        Fields=("id","profile_id","user_id")
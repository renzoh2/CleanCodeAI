from graphene_django import DjangoObjectType

from web_backend.system_app.models import (
    User,
    Profile,
    UserProfile
)

class UserTypes(DjangoObjectType):
    class Meta:
        model=User

class ProfileTypes(DjangoObjectType):
    class Meta:
        model=Profile

class UserProfileTypes(DjangoObjectType):
    class Meta:
        model=UserProfile
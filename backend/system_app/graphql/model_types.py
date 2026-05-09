from graphene_django import DjangoObjectType

from system_app.models import (
    User,
    Profile,
    UserProfile
)

class UserTypes(DjangoObjectType):
    class Meta:
        model=User
        name="User"

class ProfileTypes(DjangoObjectType):
    class Meta:
        model=Profile
        name="Profile"

class UserProfileTypes(DjangoObjectType):
    class Meta:
        model=UserProfile
        name="UserProfile"
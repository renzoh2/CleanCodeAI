from graphene_django import DjangoObjectType

from apps.authentication.models import (
    UserAccount,
    UserProfile
)

class UserAccountTypes(DjangoObjectType):
    class Meta:
        model=UserAccount
        name="UserAccount"

class UserProfileTypes(DjangoObjectType):
    class Meta:
        model=UserProfile
        name="UserProfile"
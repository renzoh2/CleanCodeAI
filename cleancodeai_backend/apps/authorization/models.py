from django.db import models
from django.db.models.functions import Now
from apps.profiles.models import Profile
from apps.authentication.models import UserAccount

class Policy(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class PolicyAssignment(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    policy = models.ForeignKey(Policy, db_column="policy_id", on_delete=models.RESTRICT, related_name="policy")
    resource = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class Roles(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class Permissions(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class AccessIdentity(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    user_account = models.ForeignKey(UserAccount, db_column="user_id", on_delete=models.RESTRICT, related_name="user_account")
    profile = models.ForeignKey(Profile, db_column="profile_id", on_delete=models.RESTRICT, related_name="profile")
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())
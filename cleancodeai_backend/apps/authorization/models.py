from django.db import models
from django.db.models.functions import Now
from apps.profiles.models import Profile
from apps.authentication.models import UserAccount

class Roles(models.Model):
    id          = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    name        = models.CharField(max_length=255)
    is_active   = models.BooleanField()
    created_at  = models.DateTimeField(db_default=Now())
    updated_at  = models.DateTimeField(db_default=Now())

class Permissions(models.Model):
    id          = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    name        = models.CharField(max_length=255)
    resource    = models.CharField(max_length=255)
    action      = models.CharField(max_length=255)
    is_active   = models.BooleanField()
    created_at  = models.DateTimeField(db_default=Now())
    updated_at  = models.DateTimeField(db_default=Now())

class RolePermissions(models.Model):
    id          = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    role        = models.ForeignKey(Roles, db_column="role_id", on_delete=models.RESTRICT, related_name="role_permissions")
    permission  = models.ForeignKey(Permissions, db_column="permission_id", on_delete=models.RESTRICT, related_name="role_permissions")
    effect      = models.CharField(max_length=255) 
    is_active   = models.BooleanField()
    created_at  = models.DateTimeField(db_default=Now())
    updated_at  = models.DateTimeField(db_default=Now())

class UserProfile(models.Model):
    id              = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    user_account    = models.ForeignKey(UserAccount, db_column="user_account_id", on_delete=models.RESTRICT, related_name="user_profile")
    profile         = models.ForeignKey(Profile, db_column="profile_id", on_delete=models.RESTRICT, related_name="user_profile")
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(db_default=Now())

class Organization(models.Model):
    id          = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    name        = models.CharField(max_length=255)
    is_active   = models.BooleanField()
    created_at  = models.DateTimeField(db_default=Now())
    updated_at  = models.DateTimeField(db_default=Now())

class UserOrganization(models.Model):
    id              = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    user_account    = models.ForeignKey(UserAccount, db_column="user_account_id", on_delete=models.RESTRICT, related_name="user_organization")
    organization    = models.ForeignKey(Organization, db_column="organization_id", on_delete=models.RESTRICT, related_name="user_organization")
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(db_default=Now())

class UserPermissions(models.Model):
    id              = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    user_account    = models.ForeignKey(UserAccount, db_column="user_account_id", on_delete=models.RESTRICT, related_name="user_permissions")
    role            = models.ForeignKey(Roles, db_column="role_id", on_delete=models.RESTRICT, related_name="user_permissions")
    is_active       = models.BooleanField()
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(db_default=Now())

class GroupPermissions(models.Model):
    id              = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    organization    = models.ForeignKey(Organization, db_column="organization_id", on_delete=models.RESTRICT, related_name="group_permissions")
    role            = models.ForeignKey(Roles, db_column="role_id", on_delete=models.RESTRICT, related_name="group_permissions")
    is_active       = models.BooleanField()
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(db_default=Now())
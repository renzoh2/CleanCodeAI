from django.db import models
from django.db.models.functions import Now
from apps.authentication.models import UserAccount
from apps.organization.models import Organization

class ActionPermission(models.TextChoices):
    CREATE = "create", "Create"
    READ = "read", "Read"
    UPDATE = "update", "Update"
    DELETE = "delete", "Delete"
    DOWNLOAD = "download", "Download"
    UPLOAD = "upload", "Upload"

class Role(models.Model):
    id          = models.UUIDField(
                    primary_key=True, 
                    db_default=models.Func(function='uuidv7')
                )
    name        = models.CharField(max_length=255)
    is_active   = models.BooleanField(
                    default=True, 
                    db_default=True
                )
    created_at  = models.DateTimeField(
                    default=Now(),
                    db_default=Now()
                )
    updated_at  = models.DateTimeField(
                    db_default=Now(), 
                    auto_now=True
                )
    
    class Meta:
        db_table = "Role"

class Permission(models.Model):
    id          = models.UUIDField(
                    primary_key=True, 
                    db_default=models.Func(function='uuidv7')
                )
    name        = models.CharField(max_length=255)
    resource    = models.CharField(max_length=255)
    action      = models.CharField(
                    max_length=255, 
                    choices=ActionPermission.choices
                )
    is_active   = models.BooleanField(
                    default=True, 
                    db_default=True
                )
    created_at  = models.DateTimeField(db_default=Now())
    updated_at  = models.DateTimeField(
                    db_default=Now(), 
                    auto_now=True
                )
    
    class Meta:
        db_table = "Permission"

class RolePermission(models.Model):
    id          = models.UUIDField(
                    primary_key=True, 
                    db_default=models.Func(function='uuidv7')
                )
    role        = models.ForeignKey(
                    Role, 
                    db_column="role_id", 
                    on_delete=models.RESTRICT, 
                    related_name="role_permission"
                )
    permission  = models.ForeignKey(
                    Permission, 
                    db_column="permission_id", 
                    on_delete=models.RESTRICT, 
                    related_name="role_permission"
                )
    is_active   = models.BooleanField(
                    default=True, 
                    db_default=True
                )
    created_at  = models.DateTimeField(
                    default=Now(),
                    db_default=Now()
                )
    updated_at  = models.DateTimeField(
                    db_default=Now(), 
                    auto_now=True
                )
    
    class Meta:
        db_table = "RolePermission"



class UserRole(models.Model):
    id              = models.UUIDField(
                        primary_key=True, 
                        db_default=models.Func(function='uuidv7')
                    )
    user_account    = models.ForeignKey(
                        UserAccount, 
                        db_column="user_account_id", 
                        on_delete=models.RESTRICT, 
                        related_name="user_role"
                    )
    role            = models.ForeignKey(
                        Role, 
                        db_column="role_id", 
                        on_delete=models.RESTRICT, 
                        related_name="user_role"
                    )
    is_active       = models.BooleanField(
                        default=True, 
                        db_default=True
                    )
    created_at      = models.DateTimeField(
                        default=Now(),
                        db_default=Now()
                    )
    updated_at      = models.DateTimeField(
                        db_default=Now(), 
                        auto_now=True
                    )
    
    class Meta:
        db_table = "UserRole"

class OrganizationRole(models.Model):
    id              = models.UUIDField(
                        primary_key=True, 
                        db_default=models.Func(function='uuidv7')
                    )
    organization    = models.ForeignKey(
                        Organization, 
                        db_column="organization_id", 
                        on_delete=models.RESTRICT, 
                        related_name="organization_role"
                    )
    role            = models.ForeignKey(
                        Role, 
                        db_column="role_id", 
                        on_delete=models.RESTRICT, 
                        related_name="organization_role"
                    )
    is_active       = models.BooleanField(
                        default=True, 
                        db_default=True
                    )
    created_at      = models.DateTimeField(
                        default=Now(),
                        db_default=Now()
                    )
    updated_at      = models.DateTimeField(
                        db_default=Now(), 
                        auto_now=True
                    )

    class Meta:
        db_table = "OrganizationRole"
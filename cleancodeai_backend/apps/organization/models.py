from django.db import models
from django.db.models.functions import Now
from apps.authentication.models import UserAccount


class Organization(models.Model):
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
        db_table = "Organization"

class UserOrganization(models.Model):
    id              = models.UUIDField(
                        primary_key=True, 
                        db_default=models.Func(function='uuidv7')
                    )
    user_account    = models.ForeignKey(
                        UserAccount, 
                        db_column="user_account_id", 
                        on_delete=models.RESTRICT, 
                        related_name="user_organization"
                    )
    organization    = models.ForeignKey(
                        Organization, 
                        db_column="organization_id", 
                        on_delete=models.RESTRICT, 
                        related_name="user_organization"
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
        db_table = "UserOrganization"

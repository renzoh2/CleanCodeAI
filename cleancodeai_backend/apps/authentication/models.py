from django.db import models
from django.db.models.functions import Now
from apps.user_profile.models import Profile

class UserAccount(models.Model):
    id              = models.UUIDField(
                        primary_key =   True, 
                        db_default  =   models.Func(function='uuidv7')
                    )
    email_address   = models.CharField(
                        max_length  =   255, 
                        db_index    =   True
                    )
    password        = models.CharField(max_length=255)
    is_active       = models.BooleanField()
    is_locked       = models.BooleanField()
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(
                        db_default  =   Now(), 
                        auto_now    =   True
                    )

    class Meta:
        db_table = "UserAccount"

class UserProfile(models.Model):
    id              = models.UUIDField(
                        primary_key =   True, 
                        db_default  =   models.Func(function='uuidv7')
                    )
    user_account    = models.ForeignKey(
                        UserAccount, 
                        db_column   =   "user_account_id", 
                        on_delete   =   models.RESTRICT, 
                        related_name=   "user_profile"
                    )
    profile         = models.ForeignKey(
                        Profile, 
                        db_column   =   "profile_id", 
                        on_delete   =   models.RESTRICT, 
                        related_name=   "user_profile"
                    )
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(
                        db_default  =   Now(), 
                        auto_now    =   True
                    )
    
    class Meta:
        db_table = "UserProfile"

class PasswordResetRequest(models.Model):
    id              = models.UUIDField(
                        primary_key =   True, 
                        db_default  =   models.Func(function='uuidv7')
                    )
    user_account    = models.ForeignKey(
                        UserAccount, 
                        db_column   =   "user_account_id", 
                        on_delete   =   models.RESTRICT, 
                        related_name=   "password_reset_request"
                    )
    email_address   = models.CharField(
                        max_length  =   255, 
                        db_index    =   True
                    )
    token_password  = models.CharField(max_length=255)
    requested_on    = models.DateTimeField(db_default=Now())
    is_used         = models.BooleanField()
    is_expired      = models.BooleanField()
    expires_at      = models.DateTimeField()
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(
                        db_default  =   Now(),
                        auto_now    =   True
                    )
    class Meta:
        db_table = "PasswordResetRequest"

class AuthenticationOTP(models.Model):
    id              = models.UUIDField(
                        primary_key =   True, 
                        db_default  =   models.Func(function='uuidv7')
                    )
    user_account    = models.ForeignKey(
                        UserAccount, 
                        db_column   =   "user_account_id", 
                        on_delete   =   models.RESTRICT, 
                        related_name=   "user_account"
                    )
    code            = models.CharField(max_length=255)
    requested_on    = models.DateTimeField(db_default=Now())
    is_approved     = models.BooleanField()
    is_expired      = models.BooleanField()
    expires_at      = models.DateTimeField()
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(
                        db_default  =   Now(),
                        auto_now    =   True
                    )
    
    class Meta:
        db_table = "AuthenticationOTP"


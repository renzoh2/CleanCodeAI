from django.db import models
from django.db.models.functions import Now
class UserAccount(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    email_address = models.CharField(max_length=255, db_index=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField()
    is_locked = models.BooleanField()
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class PasswordResetRequest(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    user_account = models.ForeignKey(UserAccount, db_column="user_account_id", on_delete=models.RESTRICT, related_name="user_account")
    email_address = models.CharField(max_length=255, db_index=True)
    token_password = models.CharField(max_length=255)
    requested_on = models.DateTimeField(db_default=Now())
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(db_default=Now())

class AuthenticationOTP(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    user_account = models.ForeignKey(UserAccount, db_column="user_account_id", on_delete=models.RESTRICT, related_name="user_account")
    code = models.CharField(max_length=255)
    is_approved = models.BooleanField()
    requested_on = models.DateTimeField(db_default=Now())
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(db_default=Now())


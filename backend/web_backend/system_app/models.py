import uuid6
from django.db import models
from django.db.models.functions import Now

class User(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    password_hashed = models.CharField(max_length=255)
    is_active = models.BooleanField()
    is_locked = models.BooleanField()
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())
    
    def __str__(self):
        return self.id

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True)
    middle_initial = models.CharField(max_length=255, null=True)
    prefix_name = models.CharField(max_length=255, null=True)
    suffix_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

    def __str__(self):
        return self.id

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    user_id = models.ForeignKey(User, db_column="user_id", on_delete=models.RESTRICT, related_name="users")
    profile_id = models.ForeignKey(Profile, db_column="profile_id", on_delete=models.DO_NOTHING, related_name="profiles")
    created_at = models.DateTimeField(db_default=Now())

    def __str__(self):
        return self.id
    

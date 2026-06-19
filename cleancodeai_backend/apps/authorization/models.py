from django.db import models
from django.db.models.functions import Now

class Users(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    email_address = models.CharField(max_length=255, db_index=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField()
    is_locked = models.BooleanField()
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())
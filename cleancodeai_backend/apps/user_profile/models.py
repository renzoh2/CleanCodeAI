from django.db import models
from django.db.models.functions import Now

class Profile(models.Model):
    id              = models.UUIDField(
                        primary_key =   True, 
                        db_default  =   models.Func(function='uuidv7')
                    )
    last_name       = models.CharField(max_length=255)
    first_name      = models.CharField(max_length=255)
    middle_name     = models.CharField(
                        max_length  =   255, 
                        null        =   True
                    )
    middle_initial  = models.CharField(
                        max_length  =   255, 
                        null        =   True
                    )
    prefix_name     = models.CharField(
                        max_length  =   255, 
                        null        =   True
                    )
    suffix_name     = models.CharField(
                        max_length  =   255, 
                        null        =   True
                    )
    email_address   = models.CharField(max_length=255)
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(
                        db_default  =   Now(), 
                        auto_now    =   True
                    )
    
    class Meta:
        db_table = "Profile"

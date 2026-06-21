from django.db import models
from django.db.models.functions import Now

class AuditLog(models.Model):
    id          = models.UUIDField(
                    primary_key=True, 
                    db_default=models.Func(function='uuidv7')
                )
    profile_id  = models.UUIDField()
    action      = models.CharField(max_length=255)
    entity_type = models.CharField(max_length=255)
    entity_id   = models.UUIDField()
    old_data    = models.TextField()
    new_data    = models.TextField()
    created_at  = models.DateTimeField(db_default=Now())

    class Meta:
        db_table = "AuditLog"

class AccessLog(models.Model):
    id                  = models.UUIDField(
                            primary_key=True, 
                            db_default=models.Func(function='uuidv7')
                        )
    user_account_id     = models.UUIDField()
    session_id          = models.UUIDField()
    request_id          = models.UUIDField()
    action              = models.CharField(max_length=255)
    method              = models.CharField(max_length=255)
    endpoint            = models.CharField(max_length=255)
    resource_type       = models.CharField(max_length=255)
    resource_id         = models.CharField(max_length=255)
    ip_address          = models.CharField(max_length=255)
    user_agent          = models.TextField()
    status_code         = models.CharField(max_length=255)
    response_time_ms    = models.DateTimeField(db_default=Now())
    created_at          = models.DateTimeField(db_default=Now())

    class Meta:
        db_table = "AccessLog"

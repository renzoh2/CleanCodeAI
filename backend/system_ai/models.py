from django.db import models
from django.db.models.functions import Now
from system_app.models import Profile
class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    profile_id = models.ForeignKey(Profile, db_column="profile_id", on_delete=models.RESTRICT, related_name="profile")
    status = models.CharField(max_length=255)
    visibility = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class ConversationSettings(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    conversation_id = models.ForeignKey(Conversation, db_column="conversation_id", on_delete=models.CASCADE, related_name="model") 
    
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class ModelContext(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    provider_name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    api_key=models.TextField()
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class Agent(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    model_context_id = models.ForeignKey(ModelContext, db_column="model_context_id", on_delete=models.DO_NOTHING, related_name="model_context")
    display_name = models.CharField(max_length=255)
    system_prompt = models.TextField()
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class MessageContext(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    agent_id = models.ForeignKey(Agent, db_column="agent_id", on_delete=models.DO_NOTHING, related_name="agent")
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now()) 
    
class Message(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    message_context_id = models.ForeignKey(MessageContext, db_column="message_context_id", on_delete=models.RESTRICT, related_name="message_context")
    message = models.TextField()
    role = models.CharField(max_length=200)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())

class MessageAdjustment(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))

class MessageAttachments(models.Model):
    id = models.UUIDField(primary_key=True, db_default=models.Func(function='uuidv7'))
    message_id = models.ForeignKey(MessageContext, db_column="message_id", on_delete=models.RESTRICT, related_name="message_context")
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100)
    file_storage_link = models.TextField()
    status = models.BooleanField()
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(db_default=Now())



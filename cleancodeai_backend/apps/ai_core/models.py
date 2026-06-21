from django.db import models
from django.db.models.functions import Now
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.userprofile.models import Profile

class AgentType(models.TextChoices):
    CONVERSATIONAL  = "conversational", "Conversational"
    TOOL            = "tool", "Tool"
    RAG             = "rag", "RAG"
    REACT           = "react", "ReAct"

class ConversationStatus(models.TextChoices):
    ACTIVE      = "active", "Active"
    ARCHIVED    = "archived", "Archived"
    DELETED     = "deleted", "Deleted"

class MessageType(models.TextChoices):
    NORMAL      = "normal", "Normal"
    SUMMARIZED  = "summarized", "Summarized"
    CONTEXT     = "context", "context"

class MessageRole(models.TextChoices):
    SYSTEM    = "system",    "System"
    USER      = "user",      "User"
    ASSISTANT = "assistant", "Assistant"
    TOOL      = "tool",      "Tool"

class AttachmentStatus(models.TextChoices):
    PENDING   = "pending",   "Pending"
    PROCESSED = "processed", "Processed"
    FAILED    = "failed",    "Failed"

class LLMProvider(models.Model):
    id              = models.UUIDField(
                        primary_key=True, 
                        db_default=models.Func(function='uuidv7')
                    )
    name            = models.CharField(max_length=255)
    display_name    = models.CharField(max_length=255)
    api_key         = models.TextField()
    base_url        = models.URLField()
    is_active       = models.BooleanField(
                        default=True, 
                        db_default=True
                    )
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(
                        db_default=Now(), 
                        auto_now=True
                    )

    class Meta:
        db_table = "LLMProvider"
    
class Agent(models.Model):
    id              = models.UUIDField(
                        primary_key=True, 
                        db_default=models.Func(function='uuidv7')
                    )
    provider        = models.ForeignKey(
                        Profile, 
                        db_column="provider_id", 
                        on_delete=models.RESTRICT, 
                        related_name="agent"
                    )
    agent_type      = models.CharField(
                        max_length=50, 
                        choices=AgentType.choices, 
                        default=AgentType.CONVERSATIONAL
                    )
    display_name    = models.CharField(max_length=255)
    model_name      = models.CharField(max_length=255)
    system_prompt   = models.TextField(blank=True)
    temperature     = models.FloatField(
                        default=1.0,
                        validators=[
                            MinValueValidator(0.0), 
                            MaxValueValidator(2.0)
                        ],
                    )
    top_k           = models.IntegerField(
                        default=50, 
                        validators=[MinValueValidator(1)]
                    )
    top_p           = models.FloatField(
                        default=1.0,
                        validators=[
                            MinValueValidator(0.0),
                            MaxValueValidator(1.0)
                        ],
                    )
    max_tokens      = models.IntegerField(
                        default=1024, 
                        validators=[MinValueValidator(1)]
                    )
    is_active       = models.BooleanField(
                        default=True, 
                        db_default=True
                    )
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(
                        db_default=Now(),
                        auto_now=True
                    )

    class Meta:
        db_table = "Agent"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(temperature__gte=0.0) & models.Q(temperature__lte=2.0),
                name="temperature_agent_check_validator",
            )
        ]

class Conversation(models.Model):
    id                      = models.UUIDField(
                                primary_key=True, 
                                db_default=models.Func(function='uuidv7')
                            )
    profile                 = models.ForeignKey(
                                Profile, 
                                db_column="profile_id", 
                                on_delete=models.RESTRICT, 
                                related_name="conversation"
                            )
    title                   = models.CharField(max_length=255)
    status                  = models.CharField(
                                max_length=255, 
                                choices=ConversationStatus.choices, 
                                default=ConversationStatus.ACTIVE
                            )
    summary_sequence_index  = models.IntegerField()
    created_at              = models.DateTimeField(db_default=Now())
    updated_at              = models.DateTimeField(
                                db_default=Now(), 
                                auto_now=True
                            )

    class Meta:
        db_table = "Conversation"

class ConversationSetting(models.Model):
    id              = models.UUIDField(
                        primary_key=True, 
                        db_default=models.Func(function='uuidv7')
                    )
    conversation    = models.ForeignKey(
                        Conversation, 
                        db_column="conversation_id", 
                        on_delete=models.CASCADE, 
                        related_name="conversation_setting"
                    ) 
    system_prompt   = models.TextField(
                        blank=True, 
                        null=True
                    )
    temperature     = models.FloatField(
                        blank=True, 
                        null=True,
                        validators=[
                            MinValueValidator(0.0), 
                            MaxValueValidator(2.0)
                        ],
                    )
    max_tokens      = models.IntegerField(
                        blank=True, 
                        null=True, 
                        validators=[MinValueValidator(1)]
                    )
    created_at      = models.DateTimeField(db_default=Now())
    updated_at      = models.DateTimeField(
                        db_default=Now(),
                        auto_now=True
                    )

    class Meta:
        db_table = "ConversationSetting"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(temperature__gte=0.0) & models.Q(temperature__lte=2.0),
                name="temperature_setting_check_validator",
            )
        ]

class ConversationMessage(models.Model):
    id                  = models.UUIDField(
                            primary_key=True, 
                            db_default=models.Func(function='uuidv7')
                        )
    conversation        = models.ForeignKey(
                            Conversation, 
                            db_column="conversation_id", 
                            on_delete=models.CASCADE, 
                            related_name="conversation_message"
                        )
    role                = models.CharField(max_length=50, choices=MessageRole.choices)
    content             = models.TextField()
    sequence            = models.PositiveIntegerField(editable=False)
    iteration           = models.PositiveIntegerField(default=1, editable=False)
    message_type        = models.CharField(
                            max_length=50, 
                            choices=MessageType.choices, 
                            default=MessageType.NORMAL
                        )
    token_count         = models.IntegerField(default=0)
    is_active_iteration = models.BooleanField(
                            default=True, 
                            db_default=True
                        )
    is_visible          = models.BooleanField(
                            default=True, 
                            db_default=True
                        )
    is_failed           = models.BooleanField(
                            default=False, 
                            db_default=False
                        )
    is_summarized       = models.BooleanField(
                            default=False, 
                            db_default=False
                        )
    created_at          = models.DateTimeField(db_default=Now())
    updated_at          = models.DateTimeField(
                            db_default=Now(),
                            auto_now=True
                        )

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.sequence:
                last_sequence = (
                    ConversationMessage.objects
                    .filter(conversation=self.conversation)
                    .aggregate(models.Max("sequence"))["sequence__max"]
                )
                self.sequence = (last_sequence or 0) + 1

            last_iteration = (
                ConversationMessage.objects
                .filter(conversation=self.conversation, sequence=self.sequence)
                .aggregate(models.Max("iteration"))["iteration__max"]
            )
            self.iteration = (last_iteration or 0) + 1

        super().save(*args, **kwargs)

    class Meta:
        db_table = "ConversationMessage"
        constraints = [
            models.UniqueConstraint(
                fields=["conversation", "sequence", "iteration"],
                name="unique_message_sequence_iteration",
            )
        ]

class MessageAttachment(models.Model):
    id                      = models.UUIDField(
                                primary_key=True, 
                                db_default=models.Func(function='uuidv7')
                            )
    conversation_message    = models.ForeignKey(
                                ConversationMessage,
                                db_column="conversation_message_id",
                                on_delete=models.CASCADE,
                                related_name="message_attachment",
                            )
    file_name               = models.CharField(max_length=255)
    file_type               = models.CharField(max_length=100)
    file_size_bytes         = models.BigIntegerField(default=0)
    file_storage_link       = models.TextField()
    status                  = models.CharField(
                                max_length=50,
                                choices=AttachmentStatus.choices,
                                default=AttachmentStatus.PENDING,
                            )
    created_at              = models.DateTimeField(db_default=Now())
    updated_at              = models.DateTimeField(
                                db_default=Now(),
                                auto_now=True
                            )

    class Meta:
        db_table = "MessageAttachments"
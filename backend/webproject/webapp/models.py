from django.db import models

class User(models.Model):
    id = models.UUIDField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
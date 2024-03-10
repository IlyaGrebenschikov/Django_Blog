from datetime import datetime

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(null=False)
    was_created = models.DateTimeField(default=datetime.now())

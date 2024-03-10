from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(null=False)

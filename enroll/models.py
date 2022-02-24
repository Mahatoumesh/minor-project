from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField(max_length = 30)
    password = models.TextField(max_length = 20)

    def __str__(self):
        return self.username
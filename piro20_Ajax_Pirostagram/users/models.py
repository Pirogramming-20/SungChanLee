from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    name = models.CharField('이름', max_length=20, unique=True)
    
    def __str__(self):
        return self.name
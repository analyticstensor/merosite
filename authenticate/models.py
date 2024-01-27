from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, verbose_name='email address', error_messages={'unique': 'A user with that email address already exists.'})
    first_name = models.CharField(max_length=150, verbose_name='first name')
    last_name = models.CharField(max_length=150, verbose_name='last name')

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        db_table = 'user'

    def __str__(self):
        return self.username
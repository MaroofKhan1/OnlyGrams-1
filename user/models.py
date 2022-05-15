from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import UserManager


class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures', null=False, blank=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)



    # objects = BaseUserManager()
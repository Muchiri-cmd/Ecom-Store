from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=100)
    bio=models.CharField(max_length=100)

    USERNAME_FIELD="email" #change login to email
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)#dont want one user to hv many profiles,del user del profiles
    image=models.ImageField(upload_to="image")#folder created image
    full_name=models.CharField(max_length=200,null=True,blank=True)
    bio=models.CharField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=200)
    verified=models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

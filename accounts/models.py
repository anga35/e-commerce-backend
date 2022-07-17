import email
import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email,fullname,password,**other_fields):
        user=self.model(email=email,fullname=fullname,**other_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,fullname,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        self.create_user(email=email,password=password,fullname=fullname,**other_fields)



def user_profile_dir(instance,filename):
    return f'profile_pictures/{instance.email}/{filename}'


# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(blank=False,null=False,unique=True)
    fullname=models.CharField(max_length=100,null=False,blank=False)
    profile_picture=models.ImageField(upload_to=user_profile_dir,blank=True,null=True,default=None)
    address=models.CharField(max_length=300,default=None,blank=True,null=True)
    account_balance=models.CharField(max_length=300,default='#0')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['fullname']
    objects=UserManager()

    '''
    TODO

    cart
    saved_items
    
    '''




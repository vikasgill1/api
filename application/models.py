from email import charset
import imp
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    mobile_number=models.CharField(max_length=12)
    gender=models.CharField(max_length=12,choices=(('male','male'),('female','female'),('other','other')))
    profile_image=models.ImageField(upload_to='application/profile_image')
    id_proof=models.FileField(upload_to="application/id_proof")
    def __str__(self):
        return self.username
class Product(models.Model):
    product_id=models.AutoField
    category=models.CharField(max_length=29)
    Subcategory=models.CharField(max_length=39)
    product_name=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.ImageField(upload_to='shop/images')
    product_desc=models.CharField(max_length=300)
    publish_date=models.DateField()

    def __str__(self):
        return self.product_name
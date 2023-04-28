from django.db import models

from django.utils.translation import ugettext_lazy as _
# Create your models here.
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings



CITY_CHOICES= [
        ('Nagpur', 'Nagpur'),
        ]

STATE_CHOICES= [
        ('Maharashtra', 'Maharashtra'),
        ]
STATUS_CHOICES= [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ]
class CustomUser(AbstractUser):
    email =models.EmailField(unique =True)
    name =models.CharField(max_length =255, null=True,blank=True)

   
    is_customer = models.BooleanField(default = False)
    is_shop = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    is_active =models.BooleanField(default=True) 



class NormalUser(models.Model):
    n_info= models.ForeignKey(settings.AUTH_USER_MODEL,db_index=True,on_delete =models.CASCADE)
    n_name=models.CharField(max_length =255, null=True,blank=True)
    n_city=models.CharField(max_length =255, null=True,blank=True,choices=CITY_CHOICES)
    n_state=models.CharField(max_length =255, null=True,blank=True,choices=STATE_CHOICES)
    n_phone=models.CharField(max_length =255, null=True,blank=True)
    n_address=models.CharField(max_length =255, null=True,blank=True)

class Shop(models.Model):

    s_info= models.ForeignKey(settings.AUTH_USER_MODEL,db_index=True,on_delete =models.CASCADE)
    s_image = models.ImageField(upload_to='Shop/',null=True,blank=True)
    s_name=models.CharField(max_length =255, null=True,blank=True)
    s_state=models.CharField(max_length =255, null=True,blank=True,choices=STATE_CHOICES)
    s_city=models.CharField(max_length =255, null=True,blank=True,choices=CITY_CHOICES )
    s_address=models.CharField(max_length =255, null=True,blank=True)
    s_phone=models.CharField(max_length =255, null=True,blank=True)



class ShopBrands(models.Model):
    tv_shop=models.ForeignKey( Shop,on_delete=models.CASCADE)
    tv_brand=models.CharField(max_length =255, null=True,blank=True)




class ShopService(models.Model):
    service_shop=models.ForeignKey( Shop,on_delete=models.CASCADE)
    service_category=models.CharField(max_length =255, null=True,blank=True)


class TvBrands(models.Model):
    tv_brand=models.CharField(max_length =255, null=True,blank=True)
    

class TVServices(models.Model):
    tv_service=models.CharField(max_length =255, null=True,blank=True)


class RequestApp(models.Model):
    user_info=models.ForeignKey( NormalUser,on_delete=models.CASCADE)
    shop_info=models.ForeignKey( Shop,on_delete=models.CASCADE)
    r_city=models.CharField(max_length =255, null=True,blank=True,choices=CITY_CHOICES )
    r_state=models.CharField(max_length =255, null=True,blank=True,choices=STATE_CHOICES)
    r_address=models.TextField(null=True,blank=True)
    r_TvBrand=models.CharField(max_length =255, null=True,blank=True)
    r_desc=models.CharField(max_length =255, null=True,blank=True)
    r_status=models.CharField(max_length =255, null=True,blank=True,choices=STATE_CHOICES,default="Pending" )
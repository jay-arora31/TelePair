from msilib.schema import Class
from django.forms import ModelForm

from django import forms
from datetime import datetime
from .models import *

from django.contrib.auth.forms import UserCreationForm,UserChangeForm ,PasswordChangeForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Row, Column, Submit
from django.contrib.auth.forms import AuthenticationForm
class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model =CustomUser
        fields =['email']


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')
        self.fields['password1'].help_text =""
        self.fields['email'].help_text =""
    
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'

        self.helper = FormHelper()
        self.helper.layout=Layout(
            
            'email',
            'password1',
            Submit('submit', 'Sign up')
        )



    n_info= models.ForeignKey(settings.AUTH_USER_MODEL,db_index=True,on_delete =models.CASCADE)
    n_name=models.CharField(max_length =255, null=True,blank=True)
    n_city=models.CharField(max_length =255, null=True,blank=True,choices=CITY_CHOICES)
    n_state=models.CharField(max_length =255, null=True,blank=True,choices=STATE_CHOICES)
    n_phone=models.CharField(max_length =255, null=True,blank=True)
    n_address=models.CharField(max_length =255, null=True,blank=True)
class NormalForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(NormalForm,self).__init__(*args,**kwargs)
        self.fields['n_name'].widget.attrs['class'] = 'form-control class_id form-group'
        self.fields['n_city'].widget.attrs['class'] = 'form-control class_id form-group'
        self.fields['n_state'].widget.attrs['class'] = 'form-control class_id form-group'
        self.fields['n_phone'].widget.attrs['class'] = 'form-control class_id form-group'
        
     
    class Meta:
                model =NormalUser
                fields =('n_name','n_city','n_state','n_phone')
                widgets = {
     

                    }
                labels = {
                            
                             'n_name': (' Name'),
                             'n_city': ('City'),
                             'n_state': ('State'),
                             'n_phone': ('Phone No.'),
                         
                }  


class ShopProfileCompleteForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ShopProfileCompleteForm,self).__init__(*args,**kwargs)
        self.fields['s_image'].widget.attrs['class'] = 'form-control class_id form-group'
        self.fields['s_name'].widget.attrs['class'] = 'form-control class_id form-group'
        self.fields['s_state'].widget.attrs['class'] = 'form-control class_id form-group'
        self.fields['s_city'].widget.attrs['class'] = 'form-control class_id form-group'
        self.fields['s_address'].widget.attrs['class'] = 'form-control class_id form-group'
        self.fields['s_phone'].widget.attrs['class'] = 'form-control class_id form-group'
     
    class Meta:
                model =Shop
                fields =('s_image','s_name','s_phone','s_address','s_state','s_city')
                widgets = {
     

                    }
                labels = {
                            
                             's_name': ('Shop Name'),
                             's_phone': ('Shop Phone Number'),
                             's_state': ('Shop State'),
                             's_city': ('Shop City'),
                             's_address': ('Shop Address'),
                             's_image': ('Shop Image'),
                }    

class editShopProfileComplete(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(editShopProfileComplete,self).__init__(*args,**kwargs)
        self.fields['s_name'].widget.attrs['class'] = 'form-control class_id form-group jk'
        self.fields['s_state'].widget.attrs['class'] = 'form-control class_id form-group jk'
        self.fields['s_city'].widget.attrs['class'] = 'form-control class_id form-group jk'
        self.fields['s_address'].widget.attrs['class'] = 'form-control class_id form-group jk'
        self.fields['s_phone'].widget.attrs['class'] = 'form-control class_id form-group jk'
     
    class Meta:
                model =Shop
                fields =('s_name','s_phone','s_address','s_state','s_city')
                widgets = {
     

                    }
                labels = {
                            
                             's_name': ('Shop Name'),
                             's_phone': ('Shop Phone Number'),
                             's_state': ('Shop State'),
                             's_city': ('Shop City'),
                             's_address': ('Shop Address'),
                }    

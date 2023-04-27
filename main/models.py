#A model is the single, definitive source of information about your data. 
#It contains the essential fields and behaviors of the data you’re storing. 
#Generally, each model maps to a single database table.


from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.



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


class UserManager(BaseUserManager):
    def create_user(self, email, password = None):

        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have an email password')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.active = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = models.CharField(max_length = 200, default = "", unique = False, blank = True)
    name = models.CharField(max_length = 200, default = "", null = False)
    email = models.EmailField(verbose_name = 'email address', max_length = 200, unique = True)
    confirm_password = models.CharField(max_length = 200, default = "", null = False)
    is_company = models.BooleanField(default = False)
    is_normal = models.BooleanField(default = False)
    active = models.BooleanField(default = False)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):          
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

class Company(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = False)
    phone_no = models.CharField(max_length=10)

    head_office_location = models.CharField(max_length = 200, default = "", blank = True)
    image = models.ImageField(upload_to = 'pics', default = "", blank = True)

    def __str__(self):
        return self.user.name



class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = False)
    phone_no = models.CharField(max_length=10)
    image = models.ImageField(upload_to = 'pics', default = "", blank = True)
    city = models.CharField(max_length = 200, default = "", blank = True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " | " + self.user.email

class Category(models.Model):
    category_name = models.CharField(max_length=200, default ="")

    def __str__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length = 200, default = "")
    
    def __str__(self):
        return self.location_name



class Service(models.Model): 
    role = models.CharField(max_length=200,default="wedfjenj")                    
    category = models.ForeignKey(Category, default = 1, on_delete = models.CASCADE, null = True)
    location = models.ForeignKey(Location, on_delete = models.CASCADE, null = True)
    content = models.TextField()                                                      
    date_published = models.DateTimeField("date published",default= datetime.now())        
    #charges = models.IntegerField(default = 0)                                         
    company = models.ForeignKey(Company,default=2,on_delete=models.CASCADE,null=True)  
    user1 = models.ForeignKey(User,default=2,on_delete=models.CASCADE,null=True)  
    address=models.CharField(max_length=200)    
    

    #Service_image=models.ImageField(upload_to='jobs/')
  

    def __str__(self):             
        return self.role      
class ShopBrands(models.Model):
    tv_shop=models.ForeignKey( Service,on_delete=models.CASCADE)
    tv_brand=models.CharField(max_length =255, null=True,blank=True)


class ShopService(models.Model):
    service_shop=models.ForeignKey( Service,on_delete=models.CASCADE)
    service_category=models.CharField(max_length =255, null=True,blank=True)


class TvBrands(models.Model):
    tv_brand=models.CharField(max_length =255, null=True,blank=True)
    

class TVServices(models.Model):
    tv_service=models.CharField(max_length =255, null=True,blank=True)
class Application(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null = False)
    Service = models.ForeignKey(Service, on_delete = models.CASCADE, null = False)
    cover_letter = models.TextField()  
    available = models.BooleanField(default=False)
    resume = models.FileField(upload_to='documents/', blank = True)
    is_accept = models.BooleanField(default=False)
    is_reject = models.BooleanField(default=False)  
    
    def __str__(self):
        return self.student.user.first_name + " " + self.student.user.last_name + " | " + self.Service.company.user.name                                       


class Comment_model(models.Model):
    comment_id=models.IntegerField(null=True,default=0)
    comment = models.TextField(max_length = 200, default = "", blank = True)    
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.comment                                 

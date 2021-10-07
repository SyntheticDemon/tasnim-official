from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from django.db.models.expressions import Subquery
from django.db.models.fields import DateTimeField, IntegerField
from django_jalali.db import models as jmodels
import time
from django.db.models.fields.related import ForeignKey, OneToOneField
class Category(models.Model):
    name=models.TextField(max_length=200)
    url=models.TextField(max_length=200)
    def __str__(self) -> str:   
        return self.name


    
class MyUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dated_joined=DateTimeField(auto_created=True)
    address=models.TextField(max_length=200)
    zip_code=models.TextField(max_length=200)
    def __str__(self) -> str:
        return self.username

class Project(models.Model):
    نام_پروژه=models.CharField(max_length=30)    
    تاریخ=jmodels.jDateField(auto_created=True)
    توضیحات=models.TextField(max_length=300)
    def __render__(self)->str:
        return "نام_پروژه %s تاریخ اضافه شدن %s تاریخ اضافه شدن %s ".format(self.نام_پروژه,self.تاریخ,self.توضیحات)
    def __str__(self) -> str:
        return self.نام_پروژه
class Input(models.Model):
    حساب_خیر=models.TextField(max_length=16)
    نام_خیر=models.TextField(max_length=100)
    مبلغ=models.DecimalField(max_digits=30,decimal_places=0)
    نام_ورودی=models.TextField(max_length=300,verbose_name="یاد نشان")
    تاریخ=jmodels.jDateField(auto_created=True)
    input_project=models.ForeignKey(Project,on_delete=models.CASCADE,null=True,verbose_name="پروژه",related_name="related_proj")
    def __str__(self) -> str:
        return  self.نام_ورودی+" "+self.نام_خیر
class Output(models.Model):
    related_project=models.ForeignKey(Project,on_delete=models.CASCADE,null=True,verbose_name='پروژه مربوطه',related_name="پروژه_مربوطه")
    حساب_مقصد=models.TextField(max_length=16)
    نام_ورودی=models.TextField(max_length=300)
    مبلغ=models.DecimalField(max_digits=30,decimal_places=2)
    تاریخ=jmodels.jDateField(auto_created=True,default="0")
    def __str__(self) -> str:
        return self.حساب_مقصد+" "+self.نام_ورودی
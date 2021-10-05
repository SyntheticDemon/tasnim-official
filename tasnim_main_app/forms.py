from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms.models import ModelForm
from tasnim_main_app.models import *
from django import forms as fm
from django_jalali.db.models import *
from django_jalali.forms.widgets import *


class RegisterationForm(fm.Form):
    username=fm.CharField(max_length=200)
    password=fm.CharField(max_length=200)
    confirm_password=fm.CharField(max_length=200)
class LoginForm(fm.Form):
    username=fm.CharField(max_length=200)
    password=fm.CharField(max_length=200)
class ProjectForm(fm.ModelForm):
    class Meta:
        model = Project
        fields ="__all__"

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['نام_پروژه'] = jDateField

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})
     

class OutputForm(fm.ModelForm):
    class Meta:
        model = Output
        fields ="__all__"

    def __init__(self, *args, **kwargs):
        super(OutputForm, self).__init__(*args, **kwargs)
        self.fields['تاریخ_پرداخت'] = jDateField

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})
       

class InputForm(fm.ModelForm):
    class Meta:
        model = Input
        fields ="__all__"

    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        self.fields['تاریخ_پرداخت'] = jDateField
        # you can added a "class" to this fiexxld for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})
       

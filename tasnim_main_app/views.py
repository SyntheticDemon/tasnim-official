import json
from time import localtime
from django.contrib.auth.signals import user_logged_in
from django.db.models import query
from django.db.models.aggregates import Count
from django.db.models.fields import DateTimeField
from django.http import response
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
import django_jalali
from jdatetime import jalali
from tasnim_main_app.models import Category, MyUser,User
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import serializers
from django.contrib.auth import authenticate, login
from tasnim_main_app.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from itertools import chain
def input_filter_view(request):

    return render(request,'report_filter_inputs.html')

def output_filter_view(request):
    return render(request,'report_filter_outputs.html')
    
def get_charity_data():
    class Cat:
        def __init__(self,cat,subcat):
            self.cat=cat
            self.subcat=subcat
    if (User.is_active):
        data=[]
        for category in Category.objects.all():
            subcats=[]
        
            data.append(Cat(category,subcats))
   
    else:
        return False 
    return data
def password_check(passwd):
      
    val = True
      
    if len(passwd) < 8:
        return ('length should be at least 8',False)
  
    if not any(char.isdigit() for char in passwd):
        return('Password should have at least one numeral',False)
          
    if not any(char.isupper() for char in passwd):
        return('Password should have at least one uppercase letter',False)
          
    if not any(char.islower() for char in passwd):
        return('Password should have at least one lowercase letter',False)

    if val:
        return ('True',True)
def filter_fin_sets(set,request):
        project_name=request.POST['project_name']
        if (len(project_name)):
            set=set.filter(related_project__نام__contains=project_name)
        if(len(request.POST['start_date'])!=0):
            start_date=request.POST['start_date']
            set=set.filter(تاریخ__gt=start_date)
        else:
            start_date='1400-01-01' 
        if(len(request.POST['end_date'])):
            end_date=(request.POST['end_date'])
            set=set.filter(تاریخ__lte=(end_date))
        else:
            end_date=None
        return set
def filter_fin_sets_inputs(set,request):
        project_name=request.POST['project_name']
        if (len(project_name)):
            set=set.filter(input_project__نام__contains=project_name)
        if(len(request.POST['start_date'])!=0):
            start_date=request.POST['start_date']
            set=set.filter(تاریخ__gt=start_date)
        else:
            start_date='1400-01-01' 
        if(len(request.POST['end_date'])):
            end_date=(request.POST['end_date'])
            set=set.filter(تاریخ__lte=(end_date))
        else:
            end_date=None
        return set
def json_fancy_report_handler(request):
        result={}
        output_set=Output.objects.all()
        input_set=Input.objects.all()
        
        first_set=filter_fin_sets_inputs(input_set,request)
        output_set=filter_fin_sets(output_set,request)
        set=chain(first_set,output_set)
        result=serializers.serialize('json',set)
        
        return HttpResponse(result, content_type='application/json')
def calculate_total_output(project):
    sum=0
    target_outputs=Output.objects.filter(related_project=project)
    for output in target_outputs:
        sum+=output.مبلغ
    return sum
def project_report_view(request):
    total_project_output=0
    project_list=[]
    context={'proj_total_finance':[],
            'total_output':total_project_output}
    for output in Output.objects.all():
        total_project_output+=output.مبلغ
    for project in Project.objects.all():
         project_list.append((project,calculate_total_output(project)))
    context['proj_total_finance']=project_list
    context['proj_total_finance'].sort(key=lambda x:x[1],reverse=True)
    return render(request,'report.html',context)

from django.db.models import Q
def input_report_view(request):
        result={}
        set=Input.objects.all()
        min_value=int(request.POST['min'])
        
        max_value=int(request.POST['max'])
        
        donor_name=request.POST['donor_name']
        card_number=request.POST['card_number']
        if(len(donor_name)):
            set=set.filter(نام_خیر__contains=donor_name)
        if(len(card_number)):
            set=set.filter(حساب_خیر__contains=card_number)
        if(len(request.POST['start_date'])!=0):
            start_date=request.POST['start_date']
            set=set.filter(تاریخ__gt=start_date)
        else:
            start_date=None 
        if(len(request.POST['end_date'])):
            end_date=(request.POST['end_date'])
            set=set.filter(تاریخ__lte=(end_date))
        else:
            end_date=None
        set= set.filter(مبلغ__gt=(min_value))
        if(max_value!=0):
            set=set.filter(مبلغ__lte=(max_value))
        
        result=serializers.serialize('json',set)
        return HttpResponse(result, content_type='application/json')
def output_report_view(request):
        result={}
        set=Output.objects.all()
        min_value=int(request.POST['min'])
        max_value=int(request.POST['max'])
        
        project_name=request.POST['project_name']
        
        card_number=request.POST['card_number']
        if(len(card_number)):
            set=set.filter(حساب_مقصد__contains=card_number)
        if (len(project_name)):
            set=set.filter(related_project__نام_پروژه__contains=project_name)
        if(len(request.POST['start_date'])!=0):
            start_date=request.POST['start_date']
            set=set.filter(تاریخ__gt=start_date)
        else:
            start_date=None 
        if(len(request.POST['end_date'])):
            end_date=(request.POST['end_date'])
            set=set.filter(تاریخ__lte=(end_date))
        else:
            end_date=None
        set= set.filter(مبلغ__gt=(min_value))
        if(max_value!=0):
            set=set.filter(مبلغ__lte=(max_value))

        result=serializers.serialize('json',set)
        return HttpResponse(result, content_type='application/json')
def admin_view(request):
    return render(request,'login.html')
#def charity_search(request):
 #   query_text=request.POST['search-text']
  #  model_results=Good.objects.filter(description__icontains=query_text)
   # results= [result.as_json_search_response() for result in model_results]
   # return  HttpResponse(json.dumps(results), content_type="application/json")
def back_home(request):
    tab_data={'tab_data':get_charity_data()}
    return render(request,'profile.html',context=tab_data)
def view_login(request):

    if(request.method=="POST"):
        form=LoginForm(request.POST)
        if form.is_valid():
                entered_username=form.data['username']
                entered_password=form.data['password']
                target_user=User.objects.filter(username=entered_username)
                if(len(target_user)==0):
                    return render(request,"login.html",context={'error':'User not Found'})
                else:
                    correct_credentials=authenticate(request,username=entered_username,password=entered_password)
                    login(request,user=correct_credentials)
                    if(target_user[0].is_active):
                        if(correct_credentials):
                            return render(request,'logged_in.html',{'tab_data':get_charity_data()})
                        else:
                            return render(request,"login.html",context={'error':'Wrong password Try again'})
    if(request.method=="GET"):
            return render(request,'logged_in.html',{'tab_data':get_charity_data()})
    return render(request,"login.html",context={'error':'Sent Data was not valid please try again'})

def signup(request):
    return render(request,'signup.html')

def home_view(request):
    return render(request,'login.html')
def create_account(request):

    if(request.method=="POST"):
        form=RegisterationForm(request.POST)
        if form.is_valid():
            entered_username=form.data['username']
            entered_password=form.data['password']
            validate_pass=password_check(entered_password)
            if(not validate_pass[1]):
                return render(request,'signup.html',{'error':validate_pass[0]})
            else:
                if(entered_password!=form.data['confirm_password']):
                    return render(request,'signup.html',{'error':'Passwords did not match'})
                else:
                    usernames=[element.username for element in User.objects.all()]
                    if(entered_username in usernames):
                        return render(request,'signup.html',{'error':'Username exists already'})
                    new_user=User.objects.create(username=entered_username)
                    new_user.set_password(entered_password)
                    new_user.save()
                    return HttpResponseRedirect('/homepage')

    return HttpResponseRedirect('/home',200)
class ProjectCreateView(CreateView):
    model = Project
    template_name = 'create.html'
    fields = '__all__'
    success_url='/backhome/'

class InputCreateView(CreateView):
    model = Input
    template_name = 'create.html'
    fields = '__all__'
    success_url='/backhome/'

class OutputUpdateView(UpdateView):
    model = Output
    template_name = 'create.html'
    success_url='/backhome/'

    fields = '__all__'
class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'create.html'
    fields = '__all__'
    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None
    success_url='/backhome/'

class InputUpdateView(UpdateView):
    model = Input
    template_name = 'create.html'
    fields = '__all__'
    success_url='/backhome/'

class OutputCreateView(CreateView):
    model = Output
    template_name = 'create.html'
    success_url='/backhome/'

    fields = '__all__'
class ProjectListView(ListView):
    model = Project
    context_object_name='data'
    template_name = 'list_all.html'

    queryset=Project.objects.all().order_by('تاریخ')
class InputListView(ListView):
    model = Input
    context_object_name='data'
    template_name = 'list_all.html'
    queryset=Input.objects.all().order_by('تاریخ')
class OutputListView(ListView):
    model = Output
    context_object_name='data'
    template_name = 'list_all.html'
    
    queryset=Output.objects.all().order_by('تاریخ')
def InputDeleteView(request,id):

    object= Input.objects.filter(pk=id)
    object.first().delete()
    return view_login(request)
def OutputDeleteView(request,id):

    object= Output.objects.filter(pk=id)
    object.first().delete()
    return view_login(request)
def ProjectDeleteView(request,id):

    object= Project.objects.filter(pk=id)
    object.first().delete()
    return view_login(request)

class InputEditView(UpdateView):
    model = Input
    template_name = 'templates/create.html'
    fields = '__all__'
class OutputEditView(UpdateView):
    model = Output
    template_name = 'templates/create.html'
    fields = '__all__'
def home_page(request):
    tab_data={'tab_data':get_charity_data()}
    if(tab_data):
        return render(request,'logged_in.html',tab_data)
    else:
        return render(request,"login.html",context={'error':'Not logged in'})

def view_subcat(request,slug):
    data=get_charity_data()
    book_data={
                'data':data,
               }
    return render(request,"subcat.html",book_data)


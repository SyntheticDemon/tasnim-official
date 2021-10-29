"""digigoods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.conf.urls import url
from django.contrib import admin
from django.http import request
from django.urls import path
from django.urls.conf import include
from tasnim_main_app.views import *
from django.contrib.auth import login
urlpatterns = [
       path('admin/', admin.site.urls),
       path('home/',home_view,name="home"),
       path('',home_view),
       path('login/',view_login,name="login"),
       path('create_account/',create_account,name="create_account"),
       path('homepage/',home_page,name="home_page"),
       path('homepage/subcat/<slug>',view_subcat,name="subcat_route"),
       path('backhome/',back_home,name="profile_view"),
       path('login/report-home',lambda request: render(request,'fancy_report.html')),
        path('login/fancy_report',json_fancy_report_handler),
       path('login/Outputs/add',OutputCreateView.as_view()),
       path('login/Projects/add',ProjectCreateView.as_view()),
       path('login/Inputs/add',InputCreateView.as_view()),
       path('login/Outputs/delete/<int:id>',OutputDeleteView),
       path('login/Inputs/delete/<int:id>',InputDeleteView,),
       path('login/Projects/delete/<int:id>',ProjectDeleteView,name="delete_projects"),
       path('login/Projects',ProjectListView.as_view()),
       path('login/Inputs',InputListView.as_view()),
       path('login/Outputs',OutputListView.as_view()),
       path('login/Outputs/edit/<int:pk>',OutputUpdateView.as_view(),name='edit_outputs'),
       path('login/Inputs/edit/<int:pk>',InputUpdateView.as_view(),name='edit_inputs'),
       path('login/Projects/edit/<int:pk>',ProjectUpdateView.as_view(),name='edit_projects'),
       path('login/Projects/report/<int:days>',project_report_view),
       path('login/Inputs/detail_report',input_filter_view),
       path('login/Outputs/detail_report',output_filter_view),
       path('login/Inputs/get_report',input_report_view),
       path('login/Outputs/get_report',output_report_view),

]
from django.contrib import admin
from tasnim_main_app.models import *
from tasnim_main_app.models  import *

from django.template.defaulttags import register
# Register your models here.

admin.site.register(MyUser)

admin.site.register(Category)
admin.site.register(Input)
admin.site.register(Output)
admin.site.register(Project)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
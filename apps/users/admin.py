from django.contrib import admin

# Register your models here.


from django.contrib import admin
from apps.users.models import Session_Year,CustomUser,Course

from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ['username','user_type']
    
admin.site.register(CustomUser,UserModel)
admin.site.register(Course)
admin.site.register(Session_Year)

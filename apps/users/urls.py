
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [    
    
      path('login/', Login, name='login'),
     
      path('doLogin/', doLogin, name='doLogin'),
      path('doLogout/', doLogout, name='doLogout'),

      path('profile/',profile,name='profile'),
      path('Profile/update',PROFILE_UPDATE,name='profile_update'),
]





from django.urls import path
from apps.SchoolManagementSystemModules import views,adminviews
from django.contrib.auth.decorators import login_required

urlpatterns = [    
    
 
      
      path('admindashboard/',login_required(views.admindashboard), name='admindashboard'),
      
      
     
      

      
]




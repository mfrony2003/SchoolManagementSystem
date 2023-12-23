
from django.urls import path
from apps.SchoolManagementSystemModules import views,adminviews
from django.contrib.auth.decorators import login_required

urlpatterns = [    
    
 
      
      path('admindashboard/',login_required(views.admindashboard), name='admindashboard'),
      path('studentdashboard/',login_required(views.studentdashboard), name='studentdashboard'),
      path('staffdashboard/',login_required(views.staffdashboard), name='staffdashboard'),
      path('test/',login_required(views.test), name='test'),
      
      
     
      

      
]




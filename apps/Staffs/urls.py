from django.urls import path
from .views import *

urlpatterns = [        
 
    
    path('Staff/Add',ADD_STAFF,name='add_staff'),
    path('Staff/View',VIEW_STAFF,name='view_staff'),
    path('Staff/Edit/<str:id>',EDIT_STAFF,name='edit_staff'),    
    path('Staff/Delete/<str:admin>',DELETE_STAFF,name='delete_staff'),
    path('Staff/Update',UPDATE_STAFF,name='update_staff'),
   
    
    
    

     
      

      
]
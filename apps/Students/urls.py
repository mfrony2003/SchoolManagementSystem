


from django.urls import path
from .views import *

urlpatterns = [        
 
    
    path('Student/Add',ADD_STUDENT,name='add_student'),
    path('Student/View',VIEW_STUDENT,name='view_student'),
    path('Student/Edit/<str:id>',EDIT_STUDENT,name='edit_student'),    
    path('Student/Delete/<str:admin>',DELETE_STUDENT,name='delete_student'),
    path('Student/Update',UPDATE_STUDENT,name='update_student'),
    path('attendance_class',attendance_class,name='attendance-class'),
    path(r'attendance/<int:classPK>/<int:sectionID>/<int:staffID>',attendance,name='attendance-page'),
    path(r'attendance/<int:classPK>/<int:sectionID>/<int:staffID>/<str:selectedDate>',attendance,name='attendance-page-date'),
    path('save_attendance',save_attendance,name='save-attendance'),
    path(r'student_result',student_result,name='student_result'),
    path(r'Result/add/<str:id>/<str:examTypeid>',add_class_result,name='add_class_result'),
    path(r'VIEW_STUDENT_BY_CLASS/<int:classPK>/<str:id>',VIEW_STUDENT_BY_CLASS,name='VIEW_STUDENT_BY_CLASS'),
    path(r'save_result',save_result,name='save_result'),
    

    # print
      path('printClassStudent/<int:classID>/<str:examTypeID>',printClassStudent,name='printClassStudent'),
      path('printStudentResult/<str:id>/<str:examTypeid>',printStudentResult,name='printStudentResult'),
      path('printAllStudent',printAllStudent,name='printAllStudent'),      
      path(r'printattendance/<int:classPK>/<int:sectionID>/<int:staffID>',printattendance,name='printattendance'),
      path(r'printattendance/<int:classPK>/<int:sectionID>/<int:staffID>/<str:selectedDate>',printattendance,name='printattendance'),
      path(r'printroutine/<int:classPK>',printroutine,name='printroutine'),

  #routine
    path('class_routin',class_routine,name='class_routin'),
    path(r'add_class_routin/<int:classPK>',add_class_routine,name='add_class_routin'),
    path(r'save_routine',save_routine,name='save_routine'),
    path(r'delete_routine/<int:classID>/<int:routineID>',delete_routine,name='delete_routine'),
    
    
      
      
    

    
    
    
]
    
    
    

     
      

      




from django.contrib import admin




from .models import Student,Class,Attendance,ClassStudent,Section,Gender,Day,Routine,ClassRoutine,ExamType,Notice,Fee,StudentFee
# Register your models here.
admin.site.register(Student)	
admin.site.register(Class)	
admin.site.register(Attendance)	
admin.site.register(ClassStudent)	
admin.site.register(Section)	
admin.site.register(Gender)	
admin.site.register(Day)	
admin.site.register(Routine)	
admin.site.register(ClassRoutine)	
admin.site.register(ExamType)	
admin.site.register(Notice)	
admin.site.register(Fee)	
admin.site.register(StudentFee)	

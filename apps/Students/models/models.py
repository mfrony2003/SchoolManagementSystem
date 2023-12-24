from datetime import date
from django.db import models
from apps.Staffs.models import Staff

from apps.users.models import CustomUser,Session_Year
from apps.users.models.models import Course, Gender, Section

# Create your models here.


    
class Class(models.Model):
    assigned_faculty = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    assigned_section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)    
    name = models.CharField(max_length=250)

    def __str__(self):
        return "Class - " +  self.name + " Section - " + self.assigned_section.name + " " + self.assigned_faculty.admin.first_name 
     
    def today(self):
        return  date.today()
 
 
class Notice(models.Model):
    classIns = models.ForeignKey(Class,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    description = models.TextField()
    
    active= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    file = models.FileField(upload_to='media/notice',blank=True, null= True)
    def __str__(self):
        return self.title + " "  + self.classIns.name 

    
# Create Student Model
class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    student_code = models.CharField(max_length=250,blank=True, null= True)    
    student_roll = models.CharField(max_length=250,blank=True, null= True)    
    student_class = models.ForeignKey(Class,on_delete=models.DO_NOTHING)
    address = models.TextField()    
    gender = models.ForeignKey(Gender,on_delete=models.DO_NOTHING)       
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    active= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class ClassStudent(models.Model):
    classIns = models.ForeignKey(Class,on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING) 

    def __str__(self):
        return self.student.student_code

    def get_present(self):
        student =  self.student
        _class =  self.classIns
        try:
            present = Attendance.objects.filter(classIns= _class, student=student, type = 1).count()
            return present
        except:
            return 0
    
    def get_tardy(self):
        student =  self.student
        _class =  self.classIns
        try:
            present = Attendance.objects.filter(classIns= _class, student=student, type = 2).count()
            return present
        except:
            return 0

    def get_absent(self):
        student =  self.student
        _class =  self.classIns
        try:
            present = Attendance.objects.filter(classIns= _class, student=student, type = 3).count()
            return present
        except:
            return 0

class Attendance(models.Model):
    classIns = models.ForeignKey(Class,on_delete=models.DO_NOTHING)
    staff=models.ForeignKey(Staff,on_delete=models.DO_NOTHING)
    section=models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    type = models.CharField(max_length=250, choices = [('1','Present'),('2','Late'),('1','Absent')] )
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.classIns.name + "  " +self.student.student_code

class Day(models.Model):    
    name = models.CharField(max_length=250)
    def __str__(self):
        return  self.name 
    
class Routine(models.Model):        
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    day = models.ForeignKey(Day,on_delete=models.DO_NOTHING)
    start_time = models.CharField(max_length=250 )
    end_time = models.CharField(max_length=250 )
    def __str__(self):
        return 'Routine - ' +  self.day.name + " " + self.start_time + " " + self.end_time
    
class ClassRoutine(models.Model):   
    routine = models.ForeignKey(Routine,on_delete=models.CASCADE)
    classFor = models.ForeignKey(Class,on_delete=models.DO_NOTHING)
    def __str__(self):
        return 'Routine - ' + self.classFor.name 
    
class ExamType(models.Model):   
    name=models.CharField(max_length=250)
    active= models.BooleanField(default=True)

    def __str__(self):
        return  self.name 
      
class Result(models.Model):   
    Student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    Course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    ExamMark = models.FloatField(default=0 )
    CTMark = models.FloatField(default=0 )
    Total = models.FloatField(default=0 )
    PassorFail = models.CharField(max_length=100, choices = [('Pass','Pass'),('Fail','Fail')] )
    ExamType = models.ForeignKey(ExamType,on_delete=models.DO_NOTHING)  

    def __str__(self):
        return 'Result - '+ self.Course.name + self.ExamMark
    
class Fee(models.Model):    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()   

    def __str__(self):
        return f"{self.amount} - {self.description}"
    
class StudentFee(models.Model):
    Fee = models.ForeignKey(Fee,on_delete=models.DO_NOTHING)  
    Student = models.ForeignKey(Student,on_delete=models.DO_NOTHING) 
    Paid = models.BooleanField(default=False)
    pay_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.Student.admin.first_name} - {self.Fee.amount}"
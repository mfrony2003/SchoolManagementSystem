from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required






@login_required
def admindashboard(request):   
        return render(request,'admin/admin.html' )  
def staffdashboard(request):   
        return render(request,'admin/staff.html' ) 
def studentdashboard(request):   
        return render(request,'admin/student.html' ) 
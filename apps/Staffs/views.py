from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.Staffs.models import  Staff
from apps.Students.models.models import Class, ClassStudent

from apps.users.models import CustomUser


from django.contrib import messages

from apps.users.models.models import Gender


@login_required(login_url='/')
def ADD_STAFF(request):    
    gender=Gender.objects.all()
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        
        if CustomUser.objects.filter(email=email).exists():
           messages.warning(request,'Email Already Exists')
           return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
           messages.warning(request,'Username Already Exists')
           return redirect('add_staff')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2
            )
            user.set_password(password)
            user.save()
            

            staff = Staff(
                admin = user,
                address = address,                
                gender = gender,
            )
            staff.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Added Successfully  !")
            return redirect('add_staff')




    context = {        
        'gender':gender,
    }

    return render(request,'Staff/add_staff.html',context)

@login_required(login_url='/')
def VIEW_STAFF(request):

    if request.user.user_type == '1':        
        staff = Staff.objects.all()
        classIds=Class.objects.all()
        
    if request.user.user_type == '3':                     
        classIds=ClassStudent.objects.filter(
                student__admin__id = request.user.id)
        staffClass=Class.objects.filter(
                id__in = classIds).values_list('assigned_faculty').all()
        staff = Staff.objects.filter(
                id__in =staffClass).all()    
            
        
    
    gender=Gender.objects.all()

    context = {
        'staff':staff,
        'student_class':classIds,
        'gender':gender,
    }
    
    return render(request,'Staff/view_staff.html',context)

 
@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff = Staff.objects.filter(id = id)    
    gender=Gender.objects.all()
    current_gender=staff.first().gender_id
    context = {
        'staff':staff,
        'gender':gender,
        'current_gender':current_gender,

        
    }
    return render(request,'Staff/edit_staff.html',context)

@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        print(staff_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id = staff_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.address = address
        staff.gender = gender

        
        
        staff.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_staff')

    return render(request,'Staff/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request,admin):
    # staff = CustomUser.objects.get(id = admin)
    # staff.delete()
    messages.success(request,'Record Are Successfully Deleted !')
    return redirect('view_staff')

from django_xhtml2pdf.utils import generate_pdf
@login_required(login_url='/')
def printAllStaff(request):
    resp = HttpResponse(content_type='application/pdf') 
    staff = Staff.objects.all()

    context = {
        'staffs':staff,
    }
      
    result = generate_pdf( "Print/staff_list.html", file_object=resp, context=context)
    return result

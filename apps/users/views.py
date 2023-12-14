
from apps.users.backendUser import UserModelBackend
from apps.users.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout

@login_required
def profile(request):   
        user = CustomUser.objects.get(id = request.user.id)
        context = {
        "user":user,
                }    
        return render(request,'profile/profile.html',context)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #email = request.POST.get('email')
        #username = request.POST.get('username')
        password = request.POST.get('password') 
        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name

            if password !=None and password != "":
                customuser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request,'Failed To Update Your Profile')

    return render(request,'profile/profile.html')

def Login(request):   
        return render(request,'login/login.html')    

def doLogin(request):
    if request.method == 'POST':
        user=UserModelBackend.authenticate(request,
                    username=request.POST.get('email'),
                    password=request.POST.get('password'),)        
        print(user)
    if user is not None:
       print(user)
       login(request,user)
       user_type=user.user_type
       
       if user_type=='1':return redirect('admindashboard')
       elif user_type=='2':return redirect('admindashboard')
       elif user_type=='3':return redirect('admindashboard')
       
       else:
        messages.error(request,'Invalid Credentials')
        return redirect('login')
    else:
        messages.error(request,'Invalid Credentials')
        return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')
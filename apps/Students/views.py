
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.Staffs.models import Staff
from apps.Students.models.models import ClassRoutine, Day, ExamType, Fee, Month, Notice, Result, Routine, Section, StudentFee
from apps.users.models import CustomUser,Course,Session_Year
from apps.Students.models import Student,Class,ClassStudent,Attendance,Gender
from datetime import date, datetime
from django.contrib import messages

context = {
    'page_title' : 'Simple Blog Site',
    'deparment_list' : [],
    'deparment_list_limited' : []
}

@login_required(login_url='/')
def ADD_STUDENT(request):    
    student_class=Class.objects.all()
    session_year = Session_Year.objects.all()
    gender=Gender.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        student_roll=request.POST.get('student_roll')        
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender_id = request.POST.get('gender_id')        
        class_id = request.POST.get('class_id')
        session_year_id = request.POST.get('session_year_id')
        student_code = request.POST.get('student_code')

        if CustomUser.objects.filter(email=email).exists():
           messages.warning(request,'Email Already Exists')
           return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
           messages.warning(request,'Username Already Exists')
           return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()
            
            studentClass = Class.objects.get(id=class_id)
            session_year = Session_Year.objects.get(id=session_year_id)
            gender=Gender.objects.get(id=gender_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                student_code = student_code,
                student_class = studentClass,
                student_roll=student_roll,
                gender = gender,
            )
            student.save()
            classStudent= ClassStudent(
                classIns = student.student_class,
                student = student,

            )
            classStudent.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Added Successfully  !")
            return redirect('add_student')



    context = {        
        'session_year':session_year,
        'student_class':student_class,
        'gender':gender,
    }

    return render(request,'Student/add_student.html',context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
      
    if request.user.user_type == '1':        
        student_class=Class.objects.all()
        students = Student.objects.all()
        
    if request.user.user_type == '2':                     
        student_class=Class.objects.get(
                assigned_faculty__admin__id = request.user.id)
        students = Student.objects.filter(
                id__in = ClassStudent.objects.filter(
                classIns = student_class).values_list('student')).all()

    


    gender=Gender.objects.all()
    context = {
        'students':students,
        'student_class':student_class,
        'gender':gender,
    }
    return render(request,'Student/view_student.html',context)

@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)   
    session_year = Session_Year.objects.all()
    student_class=Class.objects.all()
    gender=Gender.objects.all()
    current_gender=student.first().gender_id
    current_session_year=student.first().session_year_id
    current_class=student.first().student_class_id


    context = {
        'student':student,        
        'session_year':session_year,        
        'session_year_id':student.first().session_year_id_id,
        'student_class':student_class,
        'gender':gender,
        'current_gender':current_gender,
        'current_session_year':current_session_year,
        'current_class':current_class,
    }
    return render(request,'Student/edit_student.html',context)

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')        
        gender_id = request.POST.get('gender_id')        
        student_code=request.POST.get('student_code')
        session_year_id = request.POST.get('session_year_id')
        class_id = request.POST.get('class_id')
        user = CustomUser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address        
        student.student_code=student_code

        
        
        classID = Class.objects.get(id = class_id)
        student.student_class = classID
        student.gender = Gender.objects.get(id = gender_id) 

        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()

        #ClassStudent
        classStudent=ClassStudent.objects.get(student = student.id)
        classStudent.classIns=classID
        classStudent.student=student
        classStudent.save()
                
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_student')

    return render(request,'Student/edit_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    # student = CustomUser.objects.get(id = admin)
    # student.delete()
    messages.success(request,'Record  Successfully Deleted !')
    return redirect('view_student')


#Attendance
@login_required
def attendance_class(request):
    
    if request.user.user_type == '1':
            classes = Class.objects.all()
        
    if request.user.user_type == '2': 
            classes = Class.objects.filter(assigned_faculty__admin__id = request.user.id).all()

    if request.user.user_type == '3':                     
        classIds=ClassStudent.objects.filter(
                student__admin__id = request.user.id)
        classes=Class.objects.filter(
                id__in = classIds).all()
          
       
    
        
    context['page_title'] = "Attendance Management"
    context['classes'] = classes
    
    return render(request, 'Attendance/attendance_class.html',context)


@login_required
def attendance(request,classPK = None,sectionID=None,staffID=None, selectedDate=None):
    _class = Class.objects.get(id = classPK)
    _section= Section.objects.get(id = sectionID)    
    students = Student.objects.filter(id__in = ClassStudent.objects.filter(classIns = _class).values_list('student')).all()
    if request.user.user_type == '3': 
        students= Student.objects.filter(id__in = ClassStudent.objects.filter(
                student__admin__id = request.user.id).values_list('student')).all()
    context['page_title'] = "Attendance Management"
    context['class'] = _class
    context['date'] = selectedDate
    # context['disableOptions'] = date.today() > selectedDate or selectedDate < date.today()
    att_data = {}
    for student in students:
        att_data[student.id] = {}
        att_data[student.id]['data'] = student
    if not selectedDate is None:
        cdate = datetime.strptime(selectedDate, '%Y-%m-%d')
        year = cdate.strftime('%Y')
        month = cdate.strftime('%m')
        day = cdate.strftime('%d')
        attendance = Attendance.objects.filter(attendance_date__year = year, attendance_date__month = month, attendance_date__day = day, 
                                               classIns = _class , section=_section ).all()
        for att in attendance:
            att_data[att.student.pk]['type'] = att.type
    
    context['att_data'] = list(att_data.values())
    context['students'] = students

    return render(request, 'Attendance/attendance_mgt.html',context)

@login_required
def save_attendance(request):   
    if request.method == 'POST':
        post = request.POST
        date = datetime.strptime(post['attendance_date'], '%Y-%m-%d')
        year = date.strftime('%Y')
        month = date.strftime('%m')
        day = date.strftime('%d')
        _class = Class.objects.get(id=post['classIns'])
        _staff = Staff.objects.get(id=post['staffID'])
        _section = Section.objects.get(id=post['sectionID'])
        
        
        attend=Attendance.objects.filter(attendance_date__year = year, attendance_date__month = month, 
                                  attendance_date__day = day,classIns = _class, staff=_staff, section=_section )
        print(attend)
        attend.delete()
        
        for student in post.getlist('student[]'):
            type = post['type['+student+']']
            studInstance = Student.objects.get(id = student)
            att = Attendance(student=studInstance,type = type,classIns = _class,attendance_date=post['attendance_date'],
                              staff=_staff,section=_section ).save()

    return redirect('attendance-class')



#Routine
@login_required
def class_routine(request):
    
    if request.user.user_type == '1':
        myClass = Class.objects.all()        
    if request.user.user_type == '2':                     
        myClass = Class.objects.filter(assigned_faculty__admin__id = request.user.id).all()
    if request.user.user_type == '3':                     
        classIds=ClassStudent.objects.filter(
                student__admin__id = request.user.id)
        myClass=Class.objects.filter(
                id__in = classIds).all()

    context['page_title'] = "Routine Management"
    context['myClass'] = myClass
   
    return render(request, 'Routine/view_routine.html',context)

@login_required
def add_class_routine(request,classPK = None, date=None):
    _class = Class.objects.get(id = classPK)
    _course = Course.objects.all()
    _day = Day.objects.all()
    _routine = Routine.objects.filter(id__in = ClassRoutine.objects.filter( classFor=Class.objects.get(id = classPK)).values_list('routine')).all()

    context = {        
        'class':_class,
        'course':_course,
        'day':_day,
        'routine':_routine
    }
   
    return render(request, 'Routine/add_routine.html',context)


@login_required
def save_routine(request):
    if request.method == "POST":
        class_id = request.POST.get('class_id')        
        course_id = request.POST.get('course_id')
        day_id = request.POST.get('day_id')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        print(class_id,course_id,day_id,starttime,endtime)
    
    routine = Routine(               
               course=Course.objects.get(id = course_id),
               day=Day.objects.get(id = day_id),
               start_time =starttime,
               end_time =endtime,
            )
    routine.save()

    classRoutine= ClassRoutine(
                  routine=routine,
                  classFor=Class.objects.get(id = class_id),
    )
    classRoutine.save()
   
    return redirect('add_class_routin',class_id)


@login_required
def delete_routine(request,classID = None,routineID=None):
    routine = Routine.objects.get(id = routineID)
    routine.delete()
    messages.success(request,'Record  Successfully Deleted !')
    return redirect('add_class_routin',classID)

#Routine
@login_required
def student_result(request):
    
    if request.user.user_type == '1':
        myClass = Class.objects.all()
        
    if request.user.user_type == '2':
        myClass = Class.objects.filter(assigned_faculty__admin__id = request.user.id).all()

    if request.user.user_type == '3':                     
        classIds=ClassStudent.objects.filter(
                student__admin__id = request.user.id)
        myClass=Class.objects.filter(
                id__in = classIds).all()

    examType= ExamType.objects.all()
    context['page_title'] = "Result Management"
    context['myClass'] = myClass
    context['examType'] = examType
   
    return render(request, 'Result/view_result.html',context)

@login_required(login_url='/')
def VIEW_STUDENT_BY_CLASS(request,classPK = None,id=None):
    _student = Student.objects.filter(student_class_id = classPK) 
    
    if request.user.user_type == '3': 
        _student= Student.objects.filter(id__in = ClassStudent.objects.filter(
                student__admin__id = request.user.id).values_list('student')).all()
        
        

    _examType = ExamType.objects.filter(id = id).first()
    context = {
        'students':_student,
        'examType':_examType
    }
    return render(request,'Result/student_class_result.html',context)

@login_required
def add_class_result(request,id = None, examTypeid=None):    
    _student = Student.objects.filter(id=id).first()
    _course = Course.objects.all()
    _examType = ExamType.objects.filter(id = examTypeid).first()
    _result = Result.objects.filter(Student=_student,ExamType=_examType).all()
    ADD_EDIT= "Result/edit_result.html"  if  _result.count()>0  else "Result/add_result.html"
    context = {        
        'student':_student,      
       'course': _course,           
        'examType':_examType,
        'result':_result,
    }
   
    return render(request, ADD_EDIT,context)

@login_required
def save_result(request):
    student_id = request.POST.get('student_id')        
    examType_id = request.POST.get('examType_id')    
    _student=Student.objects.filter(id = student_id).first()   
    _examType=ExamType.objects.filter(id = examType_id).first()
    Result.objects.filter(Student=_student,ExamType=_examType).delete()
    if request.method == "POST":
        
        course_id = request.POST.getlist('course_id')
        ExamMark = request.POST.getlist('ExamMark')
        CTMark = request.POST.getlist('CTMark')
        Total= request.POST.getlist('Total')
        PassFail = request.POST.getlist('PassFail')
        

        for courseId, examMarks , ctMarks , total, passfail  in zip(course_id, ExamMark,CTMark,Total,PassFail):   
            result = Result(
                Student =_student,
                Course_id = courseId,
                ExamMark = examMarks,
                CTMark =ctMarks,
                ExamType = _examType,
                PassorFail= passfail,
                Total=total,
            
            )
            # not good practice saving data on loop
            
            result.save()
    
    return redirect('add_class_result',student_id,examType_id)

from django_xhtml2pdf.utils import generate_pdf

def printClassStudent(request,classID = None,examTypeID=None):
    resp = HttpResponse(content_type='application/pdf')

    _student = Student.objects.filter(student_class_id = classID) 
    _examType = ExamType.objects.filter(id = examTypeID).first()
   
    context = {
        'students':_student,
        'examType':_examType,
        'classID':classID,
        'examTypeID':examTypeID

    }    
    result = generate_pdf('Print/print_Student_By_Class.html', file_object=resp, context=context)
    return result
                
def printStudentResult(request,id = None, examTypeid=None):   
    resp = HttpResponse(content_type='application/pdf') 
    _student = Student.objects.filter(id=id).first()
    _course = Course.objects.all()
    _examType = ExamType.objects.filter(id = examTypeid).first()
    _result = Result.objects.filter(Student=_student,ExamType=_examType).all()   
    context = {        
        'student':_student,      
       'course': _course,           
        'examType':_examType,
        'result':_result,
    }
   
    result = generate_pdf( "Print/result.html", file_object=resp, context=context)
    return result

@login_required(login_url='/')
def printAllStudent(request):
    resp = HttpResponse(content_type='application/pdf') 
    students = Student.objects.all()

    context = {
        'students':students,
    }
      
    result = generate_pdf( "Print/student_list.html", file_object=resp, context=context)
    return result

@login_required
def printattendance(request,classPK = None,sectionID=None,staffID=None, selectedDate=None):
    resp = HttpResponse(content_type='application/pdf') 
    _class = Class.objects.get(id = classPK)
    _section= Section.objects.get(id = sectionID)    
    students = Student.objects.filter(id__in = ClassStudent.objects.filter(classIns = _class).values_list('student')).all()    
    if request.user.user_type == '3': 
        students= Student.objects.filter(id__in = ClassStudent.objects.filter(
                student__admin__id = request.user.id).values_list('student')).all()
        

    context['page_title'] = "Attendance Management"
    context['class'] = _class
    context['date'] = selectedDate    
    att_data = {}
    for student in students:
        att_data[student.id] = {}
        att_data[student.id]['data'] = student
    if not selectedDate is None:
        cdate = datetime.strptime(selectedDate, '%Y-%m-%d')
        year = cdate.strftime('%Y')
        month = cdate.strftime('%m')
        day = cdate.strftime('%d')
        attendance = Attendance.objects.filter(attendance_date__year = year, attendance_date__month = month, attendance_date__day = day, 
                                               classIns = _class , section=_section ).all()
        for att in attendance:
            att_data[att.student.pk]['type'] = att.type
    
    context['att_data'] = list(att_data.values())
    context['students'] = students

    result = generate_pdf( "Print/print_attendence.html", file_object=resp, context=context)
    return result


@login_required
def printroutine(request,classPK = None, date=None):
    resp = HttpResponse(content_type='application/pdf') 
    _class = Class.objects.get(id = classPK)
    _course = Course.objects.all()
    _day = Day.objects.all()
    _routine = Routine.objects.filter(id__in = ClassRoutine.objects.filter( classFor=Class.objects.get(id = classPK)).values_list('routine')).all()

    context = {        
        'class':_class,
        'course':_course,
        'day':_day,
        'routine':_routine
    }
   
    result = generate_pdf( "Print/print_routine.html", file_object=resp, context=context)
    return result


@login_required(login_url='/')
def VIEW_NOTICE(request,id=None):
        notice=Notice.objects.all()    
        selectedNotice=Notice.objects.filter(id=id)    
        context = {
            'notice':notice,
            'selectedNotice':selectedNotice,
        
        }
        return render(request,'Notice/notice.html',context)

@login_required(login_url='/')
def ADD_FEE(request):
        if request.method == "POST":
            amount = request.POST.get('amount')        
            description = request.POST.get('description')
            fee = Fee(               
                   amount = amount,
                   description = description,
                )
            fee.save()
        fee=Fee.objects.all()    
        
        context = {
             'fee':fee,
            }
        return render(request,'Fees/addfee.html',context)

@login_required(login_url='/')
def Delete_FEE(request,id=None):
      fee = Fee.objects.get(id = id)
      fee.delete()
      fee=Fee.objects.all()            
      context = {
             'fee':fee,
            }
      return render(request,'Fees/addfee.html',context)

@login_required(login_url='/')
def SAVE_FEE(request,id=None):
    fee = Fee.objects.all() 
    classStudents=ClassStudent.objects.all()       
    month=Month.objects.all()
    feesStudents=StudentFee.objects.all()
    if request.method == "POST":
            Fee_id = request.POST.get('Fee_id')        
            student_id = request.POST.get('student_id')
            month_id = request.POST.get('month_id')
            active = True if request.POST.get('active') is not None else False

       
            feesStudent=StudentFee(
            
                Fee=Fee.objects.get(id=Fee_id),
                Student=Student.objects.get(admin__id=student_id),
                Month=Month.objects.get(id=month_id),
                Paid=active,
             
            )
            feesStudent.save()

    context = {
             'fee': fee,
             'classStudents': classStudents,
             'month': month,
             'feesStudents':feesStudents
            }
    return render(request,'Fees/studentfees.html',context)

@login_required(login_url='/')
def delete_FEE(request,id=None):    
    studentFee = StudentFee.objects.get(id = id)
    studentFee.delete()
    messages.success(request,'Record  Successfully Deleted !')
    return redirect('SAVE_FEE')
    

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib import auth
from .models import *
def index(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        data=User.objects.filter(email=email).get()
        user=auth.authenticate(username=data.name,password=password)
        if user is not None:
            auth.login(request,User)
            return render(request,'dashboard.html')
        else:
            messages.alert(request,'Invalid email and password')
            return redirect("/")
    return render(request,"index.html")


def sign_up(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists')
            return render(request,"sign-up.html")
        else:
            User.objects.create(name=name,email=email,password=password)
            messages.success(request,'!!!!Successfully registered!!!!')
            return render(request,'index.html')
    else:
        return render(request,'sign-up.html')

def sign_in(request):
    if request.method=="POST":
        Name=request.POST['name']
        Password=request.POST['password']
        if User.objects.filter(Name=Name).exists():
            user=User.objects.get(Name=Name)
            Password=user.Password
            if User.objects.get(Password=Password):
                messages.success(request,"Login Successful")
                return render(request,'dashboard.html')
            else:
                messages.info(request,'Password Incorrect')
                return render(request,'sign-in.html')
    else:
        return render(request,'sign-in.html')


# def courses(request):
#     data=Course.objects.all()
#     return render(request,"courses.html",{'data':data})


def courses(request):
    std = Course.objects.filter(is_active=True).order_by('id')
    data=Course.objects.all()
    return render(request, 'courses.html', 
                  { 'request':request,
                      'std':std,
                      'data':data
                   
                    #   'std':AddCourses.objects.all()
                   }
                  )

def addcourses(request):
    if request.method == "POST":
        course_name= request.POST.get('course_name')
        course_fees= request.POST.get('fees')
        course_duration= request.POST.get('duration')
        course_desc= request.POST.get('desc')
        messages.success(request, "Course Added Successfully!!")
        Course.objects.create(course_name=course_name, course_fees=course_fees, course_duration= course_duration, course_text=course_desc)
    else:
        data= Course.objects.all()
        return render(request, 'courses.html', {'data':data})


        

def addstudent(request):
    if request.method =="POST":
        sname=request.POST.get('name')
        semail=request.POST.get('email')
        smobile=request.POST.get('mobile')
        scollege=request.POST.get('college')
        sdegree=request.POST.get('degree')
        std_course_id=request.POST.get('course')
        # yaha 2 din lag gaye the error solve karne ke lie , hame yaha se id leke ana tha jo ham nahi la rahe the
        std_course= Course.objects.get(id=std_course_id)

        if Student.objects.filter(email=semail).exists():
            messages.error(request,'Email already exists')
            return render(request,"viewstudents.html")
        else:
            Student.objects.create(name=sname,email=semail,mobile=smobile,college=scollege,degree=sdegree,Std_course=std_course)
            messages.success(request,'!!!! Student Successfully added!!!!')
            std=Student.objects.all()
            addcourses= Course.objects.all()
            return render(request, 'viewstudents.html', {'std':std, 'addcourses':addcourses})

    else:
        std=Student.objects.all()
        addcourses= Course.objects.all()
        return render(request, 'viewstudents.html', {'std':std, 'addcourses':addcourses})


def viewstudents(request):
    std = Student.objects.all()
    addcourses= addcourses.objects.all()
    redirect("viewstudents")
    return render(request, 'viewstudents.html', {'stu':std, 'addcourses':addcourses})



def update_view(request, uid):
    res = Course.objects.get(id=uid)
    return render(request, 'updatecourse.html', context={'std': res,})


def update_course(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        course_name= request.POST['course_name']
        course_fees= request.POST['fees']
        course_duration= request.POST['duration']
        course_desc= request.POST['desc']
        Course.objects.filter(id=uid).update(course_name=course_name,course_fees=course_fees,
                                            course_duration=course_duration,course_text=course_desc)
        # dhyan rahe uper wali line me hamne course_text name se modal field banai hai
        
        return redirect("/courses")                


def delete(request,pk):   
        Course.objects.filter(id=pk).delete()
        return redirect('/courses') 


def addteacher(request):
    return render(request,"addteacher.html")

def dashboard(request):
    return render(request,"dashboard.html")











def signup(request):
    return render(request,"sign-up.html")

def hostel(request):
    return render(request,"hostel.html")

def notification(request):
    return render(request,"notification.html")

def pg(request):
    return render(request,"pg.html")

def profiletable(request):
    return render(request,"profiletable.html")

def table(request):
    return render(request,"table.html")

def tenants(request):
    return render(request,"tenants.html")


# 
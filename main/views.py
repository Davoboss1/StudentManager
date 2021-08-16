from django.shortcuts import render, HttpResponse,redirect
from django.http.response import HttpResponseServerError
from .models import *


# Create your views here.
#Homepage view
def home(request):
    #Variable which contains error messages
    messages= ""
    if request.method == "POST":
        username = request.POST["username"]
        usertype = request.POST["type"]
        password = request.POST["password"]
        #Process login 
        if usertype=="Admin":
            try:
                admin = Admin.objects.get(User_name=username)
                if password==admin.Password:
                    request.session["loggedin_user"] = admin.User_name
                    return redirect("admin_page",user=admin.User_name)
            except:
                pass
            messages = ''' <h5 style="text-align: center; color: red;"> Wrong username or password, please try again. </h5>'''

        else:
            try:
                student = Student.objects.get(User_name=username)
                if password==student.Password:
                    request.session["loggedin_user"] = student.User_name
                    return redirect("student_page",user=student.User_name)
            except:
                pass
            messages = ''' <h5 style="text-align: center; color: red;"> Wrong username or password, please try again. </h5>'''
    return render(request,"index.html",{"messages":messages})

def admin_page(request,user):
    if request.session.get("loggedin_user") != user:
        return redirect("home")
    admin = Admin.objects.get(User_name=user)
    return render(request,"admin_page.html",{"students":admin.school.student_set.all(),"courses":admin.school.course_set.all()})

def student_page(request,user):
    if request.session.get("loggedin_user") != user:
        return redirect("home")
    student = Student.objects.get(User_name=user)
    return render(request,"student_page.html",{"student":student})

#Handles all actions on admin page
def processor(request,user):
    if request.method == "POST":
        school = Admin.objects.get(User_name=user).school
        if request.POST["type"] == "CS":
            Student.objects.create(Full_name=request.POST["fullname"],User_name=request.POST["username"],Password=request.POST["password"],school=school)
        elif request.POST["type"] == "DS":
            Student.objects.get(pk=request.POST["pk"]).delete()
        elif request.POST["type"] == "CC":
            if request.POST["course_title"]:
                Course.objects.create(Course_title=request.POST["course_title"],school=school)
        elif request.POST["type"] == "AC":
            if request.POST["student"] and request.POST["courses"]:
                student = Student.objects.get(pk=int(request.POST["student"]))
                courses_list = request.POST.getlist("courses")
                student.courses.set(courses_list)
        elif request.POST["type"] == "DC":
            Course.objects.get(pk=request.POST["pk"]).delete()

        return HttpResponse("")


def register(request):
    messages= ""
    if request.method == "POST":
        school= None
        try:
            school = School.objects.create(School=request.POST["school"])
            Admin.objects.create(Full_name=request.POST["full_name"],User_name=request.POST["user_name"],Password=request.POST["password"],school=school)
            messages = ''' <h5 style="text-align: center; color: green;"> Account successfully created. <a href="/"> Click here </a> to login. </h5>'''
        except:
            if school:
                school.delete()
            messages = ''' <h5 style="text-align: center; color: red;"> An error occured, enter valid inputs and try again. </h5>'''

    return render(request,"register.html",{"messages":messages})
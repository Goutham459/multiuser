from telnetlib import LOGOUT
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponse
from django.shortcuts import render, redirect

from app1.models import CustomUser


# Create your views here.

def home(request):
    return render(request, "home.html")

def adminsignup(request):
        if (request.method == "POST"):
            u = request.POST['u']
            p = request.POST['p']
            cp = request.POST['cp']
            fn = request.POST['fn']
            ln = request.POST['ln']
            e = request.POST['e']
            ph = request.POST['ph']
            pl = request.POST['pl']

            if (p == cp):
                user = CustomUser.objects.create_user(username=u, password=p, first_name=fn, last_name=ln, email=e,
                                                      phone=ph, place=pl)
                user.is_admin = True
                user.save()
                return home(request)
        return render(request, "adminsignup.html")
def studentsignup(request):
        if (request.method == "POST"):
            u = request.POST['u']
            p = request.POST['p']
            cp = request.POST['cp']
            fn = request.POST['fn']
            ln = request.POST['ln']
            e = request.POST['e']
            ph = request.POST['ph']
            pl = request.POST['pl']

            if (p == cp):
                user = CustomUser.objects.create_user(username=u, password=p, first_name=fn, last_name=ln, email=e,
                                                      phone=ph, place=pl)
                user.is_teacher = True
                user.save()
                return home(request)
        return render(request, "studentsignup.html")


def teachersignup(request):
        if (request.method == "POST"):
            u = request.POST['u']
            p = request.POST['p']
            cp = request.POST['cp']
            fn = request.POST['fn']
            ln = request.POST['ln']
            e = request.POST['e']
            ph = request.POST['ph']
            pl = request.POST['pl']

            if (p == cp):
                user = CustomUser.objects.create_user(username=u, password=p, first_name=fn, last_name=ln, email=e,
                                                      phone=ph, place=pl)
                user.is_teacher = True
                user.save()
                return home(request)
        return render(request, "teachersignup.html")

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username = u , password = p)

        if user and user.is_admin==True:
            login(request,user)
            return adminhome(request)

        elif user and user.is_student==True:
            login(request,user)
            return studenthome(request)

        elif user and user.is_teacher==True:
            login(request,user)
            return teacherhome(request)

        else:
            return HttpResponse("Invalid")

    return render(request,"login.html")

def adminhome(request):
    return render(request, "adminhome.html")

def studenthome(request):
    return render(request, "studenthome.html")

def teacherhome(request):
    return render(request, "teacherhome.html")


def user_logout(request):
    logout(request)
    return user_login(request)

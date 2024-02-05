"""
URL configuration for multiuser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app1 import views


from app1.views import home

app_name= 'app1'

urlpatterns = [
    path('', views.home,name="home"),
    path('adminsignup', views.adminsignup,name="adminsignup"),
    path('studentsignup', views.studentsignup,name="studentsignup"),
    path('teachersignup', views.teachersignup,name="teachersignup"),
    path('login', views.user_login,name="login"),
    path('adminhome', views.adminhome,name="adminhome"),
    path('studenthome', views.studenthome,name="studenthome"),
    path('teacherhome', views.teacherhome,name="teacherhome"),
    path('logout', views.user_logout,name="logout"),


]


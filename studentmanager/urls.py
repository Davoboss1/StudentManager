"""studentmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main.views import home,register,admin_page,processor,student_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('admin_page/<user>/', admin_page, name="admin_page"),
    path('admin_page/<user>/processor/', processor, name="processor"),
    path('student_page/<user>/', student_page, name="student_page"),

]

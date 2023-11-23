"""
URL configuration for excercise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task1/',task1,name='task1'),
    path('task2/',task2,name='task2'),
    path('task3/',task3,name='task3'),
    path('task4/',task4,name='task4'),
    path('task5/',task5,name='task5'),
    path('task6/',task6,name='task6'),
    path('task7/',task7,name='task7'),
    path('task8/',task8,name='task8'),
    path('task9/',task9,name='task9'),
     path('task10/',task10,name='task10'),
]

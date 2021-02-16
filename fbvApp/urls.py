from django.urls import path
from .views import *

urlpatterns = [
    path('students/',student_list,name='students'),
    path('students/<str:pk>',student_detail,name='student_detail')

]
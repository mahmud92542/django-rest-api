from django.urls import path
from .views import *

urlpatterns = [
    path('student/',StudentList.as_view(),name='student'),
    path('student/<str:pk>',StudentDetail.as_view(),name='student_details')

]
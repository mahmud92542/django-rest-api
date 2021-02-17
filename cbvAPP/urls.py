from django.urls import path
from .views import *

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('student',views.StudentViewSet)

# urlpatterns = [
# 	path('',include(router.urls)),
# ]

urlpatterns = [
    path('student/',StudentList.as_view(),name='student'),
    path('student/<str:pk>',StudentDetail.as_view(),name='student_details')

]
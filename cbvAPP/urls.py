from django.urls import path
from .views import *

#genericAPIView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('student',views.StudentViewSet)

# urlpatterns = [
# 	path('',include(router.urls)),
# ]

urlpatterns = [
    path('student/',StudentList.as_view(),name='student'),
    path('student/<str:pk>',StudentDetail.as_view(),name='student_details'),
    # nested serializer url
    # path('author/',AuthorListView.as_view(),name='author'),
    # path('author/<str:pk>',AuthorDetailView.as_view(),name='author_details'),
    # path('book/',BookListView.as_view(),name='book'),
    # path('book/<str:pk>',BookDetailView.as_view(),name='book_details'),

]
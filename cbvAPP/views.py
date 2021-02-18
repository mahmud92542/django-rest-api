from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


 from rest_framework import generics,mixins
# from rest_framework import viewsets



class AuthorListView(generics.ListCreateAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetriveUpdateDestroyAPIView):
	queryset= Author.objects.all()
	serializer_class = AuthorSerializer

class BookListView(generics.RetriveUpdateDestroyAPIView):
	queryset= Book.objects.all()
	serializer_class = BookSerializer


class BookDetailView(generics.RetriveUpdateDestroyAPIView):
	queryset= Book.objects.all()
	serializer_class = BookSerializer



# class StudentViewSet(viewsets.ModelViewSet):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializer





#Generic ViewSets
# class StudentList(generics.ListCreateAPIView):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializer

# class StudentDetail(generics.RetriveUpdateDestroyAPIView):
# 	queryset= Student.objects.all()
# 	serializer_class = StudentSerializer


#mixins views
# class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializer

# 	def get(self,request):
# 		return self.list(request)

# 	def post(self,request):
# 		return self.create(request)

# class StudentDetail(mixins.RetriveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializer


# 	def get(self,request,pk):
# 		return self.retrive(request,pk)

# 	def put(self,request,pk):
# 		return self.update(request,pk)

# 	def delete(self,request):
# 		return self.destroy(request,pk)



# Class Based Views
# class StudentList(APIView):

# 	def get(self,request):
# 		students = Student.objects.all()
# 		serializer = StudentSerializer(students,many=True)
# 		return Response(serializer.data)

# 	def post(self,request):
# 		serializer = StudentSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data,status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class StudentDetail(APIView):

# 	def get_object(self,pk):
# 	try:
# 		student = Student.objects.get(pk=pk)
# 	except Student.DoesNotExist:
# 		raise Http404

# 	def get(self,request,pk):
# 		student = self.get_object(pk)
# 		serializer = StudentSerializer(student)
# 		return Response(serializer.data)

# 	def put(self,request,pk):
# 		student = self.get_object(pk)
# 		serializer = StudentSerializer(student,data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self,request,pk):
# 		student = self.get_object(pk)
# 		student.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
	books = BookSerializer(read_only=True,many=True)
	class Meta:
		model = Author
		fields = "__all__"
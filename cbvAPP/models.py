from django.db import models

# Create your models here.
class Student(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=40)
	score = models.DecimalField(max_digits=10,decimal_places=3)

	def __str__(self):
		return self.name



class Author(models.Model):
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)

class Book(models.Model):
	title = models.CharField(max_length=100)
	rating = models. CharField(max_length=10)
	author = models.ForeignKey(Author,related_name=books,on_delete=models.CASCADE)
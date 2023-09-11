from django.db import models

# Create your models here.

class pet(models.Model):
    gender_options = (("male","male"),("female","female"))
    type = (("D","Dog"),("C","Cat"))
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media",default=None)
    species = models.CharField(max_length=50)
    gender = models.CharField(max_length=30,choices=gender_options)
    age = models.IntegerField()
    animal_type = models.CharField(max_length=30,choices=type,default="NA")
    price = models.FloatField(default=10)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        db_table ='PetTbl'  
    
class Student(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(default=None)
    
    class Meta:
        db_table = 'stud'
        
        
class course(models.Model):
    course_name = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
        
        
        
class Author(models.Model):
    name = models.CharField(max_length=50)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)



    
        
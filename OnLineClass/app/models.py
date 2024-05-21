from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

""" from django.db import models
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/' , blank=True, null=True)
    
    def __str__(self) :
        return self.username """

class Course(models.Model):
    title = models.CharField (max_length=200)
    description = models.TextField()
    instructor = models.OneToOneField(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    image_course = models.ImageField(upload_to='courseimg')
    
    def __str__(self) :
        return self.title
    
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course , related_name='lessons', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    image_lesson = models.ImageField(upload_to='lessonimg')
    content = models.TextField(blank=True, null=True)
    
    def __str__(self) :
        return self.title
    


 

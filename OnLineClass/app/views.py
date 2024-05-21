from django.shortcuts import render
from django.views import View

from .models import Course, Lesson
# Create your views here.

""" def base(request, *args, **kwargs):
    return render(request, "app/base.html", {}) """

def home(request, *args, **kwargs):
    return render(request, "app/home.html", {})

def about(request, *args, **kwargs):
    return render(request, "app/about.html", {})

def contact(request, *args, **kwargs):
    return render(request, "app/contact.html", {})

def courses(request, ):
    courses = Course.objects.all()
    return render(request, "app/courses.html", {'courses': courses})

class Course_details(View):
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        lessons = Lesson.objects.filter(course=course)
        return render(request, 'app/courses-details.html', {'course': course, 'lessons': lessons})


class Lesson_details(View):
 def get(self, request,pk):
    lesson=Lesson.objects.get(pk=pk)
    return render(request, 'app/lesson-details.html', locals())

""" def lesson(request, ):
    lesson = Lesson.objects.all()
    return render(request, "app/course-details.html", {'lessons': lesson}) """
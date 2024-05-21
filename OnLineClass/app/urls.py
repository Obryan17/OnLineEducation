from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),
    
    path('courses/', views.courses, name='courses'),
    
    path('courses/<int:pk>', views.Course_details.as_view(), name='course_details'),
    
    path('lesson/<int:pk>', views.Lesson_details.as_view(), name='lesson_details'),

]
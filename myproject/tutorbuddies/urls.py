from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tutors/', views.tutors, name='tutors'),

    # Student URLs
    path('student/login/', views.student_login_view, name='student_login'),
    path('student/register/', views.student_register, name='student_register'),

    # Tutor URLs
    path('tutor/login/', views.tutor_login_view, name='tutor_login'),       # Make sure you have this view in views.py
    path('tutor/register/', views.tutor_register, name='tutor_register'),

    # Parent URLs
    path('parent/login/', views.parent_login_view, name='parent_login'),   # Make sure you have this view in views.py
    path('parent/register/', views.parent_register, name='register_parent'),

    # Unified login and logout URLs
    path('login/', views.login_view, name='login'),                   # Your single login page view
    path('logout/', views.logout_view, name='logout'),
]

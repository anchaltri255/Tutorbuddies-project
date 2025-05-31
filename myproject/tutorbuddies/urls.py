
from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tutors/', views.tutors, name='tutors'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('student-login/', views.student_login, name='student_login'),
    path('tutor-login/', views.tutor_login, name='tutor_login'),
    path('register-parent/', views.register_parent, name='register_parent'),
]
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages  # optional for user feedback

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you can handle the form data as needed
            # For example, send an email or save to DB
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'tutorbuddies/contact.html', {'form': form})
def home(request):
    return render(request,'tutorbuddies/home.html')

def about(request):
    return render(request, 'tutorbuddies/about.html')

def tutors(request):
    return render(request, 'tutorbuddies/tutors.html')


def student_login(request):
    return render(request, 'tutorbuddies/student_login.html')

def tutor_login(request):
    return render(request, 'tutorbuddies/tutor_login.html')

def register_parent(request):
    if request.method == 'POST':
        # Parent Info
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        terms = request.POST.get('terms')

        # Child Info
        child_name = request.POST.get('child_name')
        child_age = request.POST.get('child_age')
        child_gender = request.POST.get('child_gender')
        child_class = request.POST.get('child_class')
        child_board = request.POST.get('child_board')
        child_school = request.POST.get('child_school')

        # Validation
        required_fields = [
            full_name, email, password, confirm_password, phone, address,
            child_name, child_age, child_gender, child_class, child_board, child_school, terms
        ]

        if not all(required_fields):
            messages.error(request, "Please fill in all required fields and accept terms.")
            return render(request, 'tutorbuddies/register_parent.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'tutorbuddies/register_parent.html')

        # TODO: Save to DB (Create Parent and Child models or use Django's built-in User with a profile)

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')  # Replace with your actual login route name

    return render(request, 'tutorbuddies/register_parent.html')

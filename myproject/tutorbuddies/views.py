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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
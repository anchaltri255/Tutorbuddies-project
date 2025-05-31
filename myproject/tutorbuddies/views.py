from django.http import HttpResponse
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login ,logout
from django.db import IntegrityError
from .forms import StudentLoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Student, Tutor, Parent, Child

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


def student_login_view(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            try:
                student = form.save()
                request.session['student_name'] = student.name  # store student name
                messages.success(request, f'You logged in successfully! Welcome, {student.name}.')
                return redirect('home')  # go to homepage
            except IntegrityError:
                form.add_error('email', 'This email is already registered.')
    else:
        form = StudentLoginForm()

    return render(request, 'tutorbuddies/student_login.html', {'form': form})

def logout_view(request):
    request.session.flush()
    return redirect('home')

def student_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        school_name = request.POST['school_name']
        gender = request.POST['gender']
        board = request.POST['board']
        city = request.POST['city']
        mobile = request.POST['mobile']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('student_register')

        if Student.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('student_register')

        hashed_password = make_password(password)

        Student.objects.create(
            name=name,
            father_name=father_name,
            mother_name=mother_name,
            school_name=school_name,
            gender=gender,
            board=board,
            city=city,
            mobile=mobile,
            email=email,
            address=address,
            password=hashed_password
        )
        messages.success(request, "Student registered successfully! Please login.")
        return redirect('student_login')

    return render(request, 'student_register.html')

def tutor_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        qualification = request.POST['qualification']
        subjects = request.POST['subjects']
        classes = request.POST['classes']
        experience = request.POST['experience']
        mode = request.POST['mode']
        city = request.POST['city']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('tutor_register')

        if Tutor.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('tutor_register')

        hashed_password = make_password(password)

        Tutor.objects.create(
            name=name,
            phone=phone,
            email=email,
            qualification=qualification,
            subjects=subjects,
            classes=classes,
            experience=int(experience),
            mode=mode,
            city=city,
            address=address,
            password=hashed_password
        )
        messages.success(request, "Tutor registered successfully! Please login.")
        return redirect('tutor_login')

    return render(request, 'tutor_register.html')

def parent_register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('parent_register')

        if Parent.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('parent_register')

        hashed_password = make_password(password)

        parent = Parent.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            password=hashed_password
        )

        child_names = request.POST.getlist('child_name[]')
        child_ages = request.POST.getlist('child_age[]')
        child_genders = request.POST.getlist('child_gender[]')
        child_classes = request.POST.getlist('child_class[]')
        child_boards = request.POST.getlist('child_board[]')
        child_schools = request.POST.getlist('child_school[]')

        for i in range(len(child_names)):
            Child.objects.create(
                parent=parent,
                name=child_names[i],
                age=int(child_ages[i]),
                gender=child_genders[i],
                class_name=child_classes[i],
                board=child_boards[i],
                school_name=child_schools[i]
            )

        messages.success(request, "Parent and children registered successfully! Please login.")
        return redirect('parent_login')

    return render(request, 'tutorbuddies/register_parent.html')

def tutor_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            tutor = Tutor.objects.get(email=email)
            if check_password(password, tutor.password):
                request.session['tutor_name'] = tutor.name
                messages.success(request, f'Welcome Tutor {tutor.name}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid password.')
        except Tutor.DoesNotExist:
            messages.error(request, 'Tutor with this email does not exist.')

    return render(request, 'tutorbuddies/tutor_login.html')

def parent_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            parent = Parent.objects.get(email=email)
            if check_password(password, parent.password):
                request.session['parent_name'] = parent.full_name
                messages.success(request, f'Welcome Parent {parent.full_name}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid password.')
        except Parent.DoesNotExist:
            messages.error(request, 'Parent with this email does not exist.')

    return render(request, 'tutorbuddies/parent_login.html')

def login_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = None
        if role == 'student':
            try:
                user = Student.objects.get(email=email)
            except Student.DoesNotExist:
                messages.error(request, 'Student with this email does not exist.')
        elif role == 'parent':
            try:
                user = Parent.objects.get(email=email)
            except Parent.DoesNotExist:
                messages.error(request, 'Parent with this email does not exist.')
        elif role == 'teacher':
            try:
                user = Tutor.objects.get(email=email)
            except Tutor.DoesNotExist:
                messages.error(request, 'Teacher with this email does not exist.')
        else:
            messages.error(request, 'Please select a valid role.')

        if user:
            if check_password(password, user.password):
                # Store user info in session based on role
                request.session['user_id'] = user.id
                request.session['user_role'] = role
                request.session['user_name'] = getattr(user, 'name', getattr(user, 'full_name', ''))
                messages.success(request, f'Welcome {request.session["user_name"]}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid password.')

    return render(request, 'tutorbuddies/login.html')

def logout_view(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('home')

def home(request):
    user_role = request.session.get('user_role')
    user_name = request.session.get('user_name')
    return render(request, 'tutorbuddies/home.html', {'user_role': user_role, 'user_name': user_name})
from django.db import models
from django.contrib.auth.hashers import make_password

class Student(models.Model):
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    board = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # hashed password
    address = models.TextField()

    def save(self, *args, **kwargs):
        # Hash password before saving if not hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Tutor(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # hashed password
    qualification = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)
    classes = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    mode = models.CharField(max_length=10)  # Online / Offline / Both
    city = models.CharField(max_length=100)
    address = models.TextField()

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Parent(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    password = models.CharField(max_length=255)  # hashed password

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    class_name = models.CharField(max_length=50)
    board = models.CharField(max_length=50)
    school_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.parent.full_name})"

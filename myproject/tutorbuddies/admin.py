from django.contrib import admin
from django import forms
from django.contrib.auth.hashers import make_password
from .models import Student, Tutor, Parent, Child

class StudentAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Student
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        confirm_pwd = cleaned_data.get('confirm_password')
        if pwd != confirm_pwd:
            raise forms.ValidationError("Passwords do not match!")
        cleaned_data['password'] = make_password(pwd)
        return cleaned_data

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm
    list_display = ['name', 'father_name', 'mother_name', 'school_name', 'gender', 'board', 'city', 'mobile', 'email', 'address']

class TutorAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Tutor
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        confirm_pwd = cleaned_data.get('confirm_password')
        if pwd != confirm_pwd:
            raise forms.ValidationError("Passwords do not match!")
        cleaned_data['password'] = make_password(pwd)
        return cleaned_data

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    form = TutorAdminForm
    list_display = ['name', 'phone', 'email', 'qualification', 'subjects', 'classes', 'experience', 'mode', 'city', 'address']

class ParentAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Parent
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        confirm_pwd = cleaned_data.get('confirm_password')
        if pwd != confirm_pwd:
            raise forms.ValidationError("Passwords do not match!")
        cleaned_data['password'] = make_password(pwd)
        return cleaned_data

class ChildInline(admin.TabularInline):
    model = Child
    extra = 1

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    form = ParentAdminForm
    list_display = ['full_name', 'email', 'phone', 'address']
    inlines = [ChildInline]

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'class_name', 'board', 'school_name', 'parent']

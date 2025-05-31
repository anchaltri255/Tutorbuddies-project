
from django import forms
from .models import Student

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")



class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
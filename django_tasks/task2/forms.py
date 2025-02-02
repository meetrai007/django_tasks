from .models import Students
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        labels = {
            'name': 'Student Name',
            'age': 'Student Age',
            'roll': 'Student Roll',
            'class_name': 'Student Class',
            'city': 'Student Address',
        }
        
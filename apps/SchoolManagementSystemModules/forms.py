from django import forms
from .models import Student,Subject,Department

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        department=  forms.ModelChoiceField(queryset=Department.objects.all(),empty_label=None, to_field_name="name")
        
        fields = ['first_name', 'roll_number', 'department']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control',}),
        }
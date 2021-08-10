from django import forms
from .models import StudentInfo

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        exclude = ("student_img", "fathers_img", "mothers_img", )

        widgets = {
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Academic Year'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Admission Date',
                                                     'type': 'date'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'shift_type': forms.Select(attrs={'class': 'form-control'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father Name'}),
            'fathers_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Father ID'}),
            'fathers_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Father Number'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother Name'}),
            'mothers_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mother ID'}),
            'mothers_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mother Number'}),
        }


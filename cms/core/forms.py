from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email',  'course', 'branch', 'current_year', 'section']
    
    # Custom validation for current_year
    def clean_current_year(self):
        current_year = self.cleaned_data.get('current_year')
        if current_year < 1 or current_year > 4:
            raise forms.ValidationError("Current Year must be between 1 and 4")
        return current_year

    # Custom validation for email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required")
        return email
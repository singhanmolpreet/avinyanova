from django import forms
from .models import AcademicRecord, ExtraCurricularActivity, SportsAchievement

class AcademicRecordForm(forms.ModelForm):
    class Meta:
        model = AcademicRecord
        fields = ['subject', 'marks_obtained', 'total_marks', 'semester', 'proof']

class ExtraCurricularForm(forms.ModelForm):
    class Meta:
        model = ExtraCurricularActivity
        fields = ['activity_name', 'description', 'date', 'proof']

class SportsAchievementForm(forms.ModelForm):
    class Meta:
        model = SportsAchievement
        fields = ['sport_name', 'achievement', 'level', 'date', 'proof']

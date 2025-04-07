from django.db import models
from django.conf import settings

class AcademicRecord(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()
    semester = models.CharField(max_length=20)
    proof = models.FileField(upload_to='proofs/academic/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"

class ExtraCurricularActivity(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    proof = models.FileField(upload_to='proofs/extracurricular/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.activity_name}"

class SportsAchievement(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sport_name = models.CharField(max_length=100)
    achievement = models.CharField(max_length=255)
    level = models.CharField(max_length=100)  # eg. Intercollege, National, etc.
    date = models.DateField()
    proof = models.FileField(upload_to='proofs/sports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.sport_name}"

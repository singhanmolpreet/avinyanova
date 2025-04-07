from django.db import models

class branch(models.TextChoices):
    CSE = 'CSE', 'Computer Science and Engineering'
    EE = 'EE', 'Electrical Engineering'
    ECE = 'ECE', 'Electronics and Communication Engineering'
    IT = 'IT', 'Information Technology'
    ME = 'ME', 'Mechanical Engineering'
    CE = 'CE', 'Civil Engineering'

class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    course=models.CharField(max_length=255)
    branch = models.CharField(max_length=3, choices=branch.choices, default=None)
    current_year = models.IntegerField(choices=[(i, i) for i in range(1, 5)], default=1)
    max_year = models.IntegerField(blank=True, null=True, editable=False)
    section = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
                                                      ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')])

    def __str__(self):
        return f"{self.name} - {self.student_id}"
    
    def save(self, *args, **kwargs):
        # Set max_year as current_year + 1 before saving
        self.max_year = self.current_year + 1
        super(Student, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
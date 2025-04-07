from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
 
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if 'role' not in extra_fields or not extra_fields['role']:
            extra_fields.setdefault('role', 'CANDIDATE')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('STUDENT','Student'),
        ('TEACHER','Teacher')
    ]
    
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=20, choices=ROLES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']    
    def __str__(self):
        return self.email


class Department(models.TextChoices):
    CSE = 'CSE', 'Computer Science and Engineering'
    EE = 'EE', 'Electrical Engineering'
    ECE = 'ECE', 'Electronics and Communication Engineering'
    IT = 'IT', 'Information Technology'
    ME = 'ME', 'Mechanical Engineering'
    CE = 'CE', 'Civil Engineering'
    

class studentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    year=models.PositiveSmallIntegerField(null=True, blank=True)
    department = models.CharField(max_length=3, choices=Department.choices, default=None)

    
    def __str__(self):
        return self.user.email
    
class teacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    image = models.ImageField(upload_to='teacher_images/', null=True, blank=True)
    department = models.CharField(max_length=3, choices=Department.choices, default=None)
    designation = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.user.email
    
from django.shortcuts import render, redirect
from .forms import StudentForm

def home(request):
    return render(request,'home.html')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the student list view or a success page
    else:
        form = StudentForm()
    return render(request, 'form.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AcademicRecordForm, ExtraCurricularForm, SportsAchievementForm
from django.http import HttpResponseForbidden

def home(request):
    return render(request, 'home.html')

@login_required(login_url= 'login')
def academic_success(request):
    return render(request, 'academic_success.html')

@login_required(login_url= 'login')
def extra_success(request):
    return render(request, 'extra_success.html')

@login_required(login_url= 'login')
def sports_success(request):
    return render(request, 'sports_success.html')

@login_required(login_url= 'login')
def student_dashboard(request):
    if request.user.role != 'STUDENT':
        return HttpResponseForbidden("You are not allowed to access this page.")
    return render(request, 'student_dashboard.html')


@login_required(login_url='login')
def upload_academic_record(request):
    if request.method == 'POST':
        form = AcademicRecordForm(request.POST, request.FILES)
        if form.is_valid():
            academic_record = form.save(commit=False)
            academic_record.student = request.user
            academic_record.save()
            return redirect('academic_success')
    else:
        form = AcademicRecordForm()
    return render(request, 'upload.html', {'form': form})


@login_required(login_url='login')
def upload_extra_curricular(request):
    if request.method == 'POST':
        form = ExtraCurricularForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.student = request.user
            record.save()
            return redirect('extra_success')
    else:
        form = ExtraCurricularForm()
    return render(request, 'upload_extra.html', {'form': form})


@login_required(login_url='login')
def upload_sports_achievement(request):
    if request.method == 'POST':
        form = SportsAchievementForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.student = request.user
            record.save()
            return redirect('sports_success')
    else:
        form = SportsAchievementForm()
    return render(request, 'upload_sports.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate,logout
from .forms import UserRegistrationForm
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib import messages
from django.utils.crypto import get_random_string


def generate_otp():
    """Generate a 6-digit OTP."""
    return str(random.randint(100000, 999999))


def send_otp_email(email, otp):
    """Send OTP to the user's email."""
    subject = 'Verify Your Email'
    message = f'Your OTP for email verification is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False  # User is not active until email verification
            user.save()

            # Generate and store OTP
            otp = generate_otp()
            request.session['otp'] = otp
            request.session['user_id'] = user.id
            request.session['email'] = user.email

            # Send OTP email
            send_otp_email(user.email, otp)

            return redirect('verify_otp')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        user_id = request.session.get('user_id')
        email = request.session.get('email')

        if entered_otp == stored_otp:
            # OTP is correct, activate the user
            user = get_object_or_404(CustomUser, id=user_id)
            user.is_active = True
            user.save()
            messages.success(request, 'Your account has been activated successfully!')

            # Clear OTP and user_id from session
            del request.session['otp']
            del request.session['user_id']
            del request.session['email']

            return redirect('login')  # Redirect to login page
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return render(request, 'verify_otp.html')
    else:
        return render(request, 'verify_otp.html')


def LoginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                # Generate and store OTP for login
                otp = generate_otp()
                request.session['otp'] = otp
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                request.session['login_attempt'] = True

                # Send OTP email
                send_otp_email(user.email, otp)
                messages.success(request, 'OTP has been sent to your email.')
                return redirect('verify_login_otp')
            else:
                messages.error(request, 'Your account is not active. Please verify your email.')
                return render(request, 'login.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def verify_login_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        user_id = request.session.get('user_id')
        email = request.session.get('email')
        login_attempt = request.session.get('login_attempt')

        if entered_otp == stored_otp and login_attempt:
            # OTP is correct, log in the user
            user = get_object_or_404(CustomUser, id=user_id)
            login(request, user)
            messages.success(request, 'You have been logged in successfully!')

            # Clear OTP and user_id from session
            del request.session['otp']
            del request.session['user_id']
            del request.session['email']
            del request.session['login_attempt']

            return redirect('home')  # Redirect to home/dashboard page
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return render(request, 'verify_login_otp.html')
    else:
        return render(request, 'verify_login_otp.html')


def LogoutPage(request):
    logout(request)
    return redirect('home')

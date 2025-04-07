# your_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import generate_response, get_student_data
from authentication.models import studentProfile

@login_required(login_url='login')
def chatbot_view(request):
    print("Chatbot view called") #add this line
    if request.method == "POST":
        print("POST request received") #add this line
        user_query = request.POST.get("user_query")
        print(f"User query: {user_query}") #add this line
        user = request.user
        print(f"User role: {user.role}") #add this line
        if user.role == "STUDENT":
            try:
                student_profile = studentProfile.objects.get(user=user)
                student_data = get_student_data(student_profile)
                print(f"Student Data: {student_data}") #add this line
                chatbot_response = generate_response(user_query, student_data)
                print(f"Chatbot response: {chatbot_response}") #add this line
                return render(request, "chatbot.html", {"chatbot_response": chatbot_response})
            except studentProfile.DoesNotExist:
                print("student profile does not exist")
                return render(request, "chatbot.html", {"error_message": "Student profile not found. Please create your profile first."})

        elif user.role == "TEACHER":
            all_student_profiles = studentProfile.objects.all()
            all_student_data = []
            for student_profile in all_student_profiles:
                all_student_data.append(get_student_data(student_profile))
            print(f"All student data: {all_student_data}") #add this line
            chatbot_response = generate_response(user_query, all_student_data)
            print(f"Chatbot response: {chatbot_response}") #add this line
            return render(request, "chatbot.html", {"chatbot_response": chatbot_response})
    else:
        print("GET request received") #add this line
    return render(request, "chatbot.html")
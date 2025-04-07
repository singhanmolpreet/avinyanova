# your_app/services.py
import google.generativeai as genai
import os
from core.models import AcademicRecord, ExtraCurricularActivity, SportsAchievement
from authentication.models import CustomUser, studentProfile

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def get_student_data(student_profile):
    academic_records = AcademicRecord.objects.filter(student=student_profile)
    extra_curriculars = ExtraCurricularActivity.objects.filter(student=student_profile)
    sports_achievements = SportsAchievement.objects.filter(student=student_profile)

    data = {
        "academic_records": [{"title": record.title, "description": record.description, "date": record.date} for record in academic_records],
        "extra_curriculars": [{"title": record.title, "description": record.description, "date": record.date} for record in extra_curriculars],
        "sports_achievements": [{"title": record.title, "description": record.description, "date": record.date} for record in sports_achievements],
    }
    return data

def generate_response(prompt, data):
    data_str = str(data)
    full_prompt = f"Given the following student data: {data_str}, answer the user's question: {prompt}"
    response = model.generate_content(full_prompt)
    return response.text
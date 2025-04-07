from django.contrib import admin
from .models import AcademicRecord, ExtraCurricularActivity,SportsAchievement


admin.site.register(AcademicRecord)
admin.site.register(ExtraCurricularActivity)
admin.site.register(SportsAchievement)
# admin.py
from django.contrib import admin
from .models import Home, Demand, Skills, Geography, WebDeveloperSalary, JobVacancyShare, CybersecuritySalary

@admin.register(Geography)
class GeographyAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'salary_table', 'vacancy_table', 'graph')  

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'text_1', 'text_2', 'image_1', 'image_2')

@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'graph_left', 'graph_right')

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'graph')

@admin.register(WebDeveloperSalary)
class WebDeveloperSalaryAdmin(admin.ModelAdmin):
    list_display = ('city', 'average_salary', 'notes')

@admin.register(JobVacancyShare)
class JobVacancyShareAdmin(admin.ModelAdmin):
    list_display = ('city', 'share', 'notes')

@admin.register(CybersecuritySalary)
class CybersecuritySalaryAdmin(admin.ModelAdmin):
    list_display = ('city', 'average_salary', 'notes')
from django.contrib import admin
from .models import Vacancy

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'salary', 'region', 'published_date')
    search_fields = ('title', 'company', 'region')
    list_filter = ('published_date', 'region')
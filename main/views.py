from django.shortcuts import render
from .models import Home, Demand, Skills, Geography, WebDeveloperSalary, JobVacancyShare, CybersecuritySalary
from .utils import get_vacancies
import os

from rest_framework import viewsets
from .serializers import (
    WebDeveloperSalarySerializer, 
    JobVacancyShareSerializer, 
    CybersecuritySalarySerializer,
    HomeSerializer,
    DemandSerializer,
    SkillsSerializer,
    GeographySerializer
)

# Create your views here.

def home(request):
    homepage = Home.objects.all()[0]
    return render(
        request,
        'main/home.html',
        context={
            'homepage': homepage,
        }
    )

def info(request):
    infopage = Demand.objects.all()[0]
    return render(
        request,
        'main/info.html',
        context={
            'infopage': infopage,
        }
    )

def geography(request):
    geographypage = Geography.objects.first()  
    context = {
        'geographypage': geographypage,
    }
    return render(request, 'main/geography.html', context)

class WebDeveloperSalaryViewSet(viewsets.ModelViewSet):
    queryset = WebDeveloperSalary.objects.all()
    serializer_class = WebDeveloperSalarySerializer

class JobVacancyShareViewSet(viewsets.ModelViewSet):
    queryset = JobVacancyShare.objects.all()
    serializer_class = JobVacancyShareSerializer

class CybersecuritySalaryViewSet(viewsets.ModelViewSet):
    queryset = CybersecuritySalary.objects.all()
    serializer_class = CybersecuritySalarySerializer

class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class GeographyViewSet(viewsets.ModelViewSet):
    queryset = Geography.objects.all()
    serializer_class = GeographySerializer

def vacancies(request):
    return render(request, 'main/vacanvies_template.html',
                  context={'vacancies': get_vacancies(), })

def skills(request):
    skillspage = Skills.objects.all()[0]
    return render(
        request,
        'main/skills.html',
        context={
            'skillspage': skillspage,
        }
    )
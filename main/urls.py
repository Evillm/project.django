from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HomeViewSet,
    DemandViewSet,
    SkillsViewSet,
    GeographyViewSet,
    WebDeveloperSalaryViewSet,
    JobVacancyShareViewSet,
    CybersecuritySalaryViewSet,
    home,  
    info,  
    geography,  
    skills,  
    vacancies,  
)

router = DefaultRouter()
router.register(r'home', HomeViewSet)
router.register(r'demand', DemandViewSet)
router.register(r'skills', SkillsViewSet)
router.register(r'geography', GeographyViewSet)
router.register(r'web-developer-salaries', WebDeveloperSalaryViewSet)
router.register(r'job-vacancy-shares', JobVacancyShareViewSet)
router.register(r'cybersecurity-salaries', CybersecuritySalaryViewSet)

urlpatterns = [
    path('', home, name='home'),  
    path('info/', info, name='info'),  
    path('geography/', geography, name='geography'),  
    path('skills/', skills, name='skills'),  
    path('vacancies/', vacancies, name='vacancies'), 
    path('api/', include(router.urls)),  
    


]
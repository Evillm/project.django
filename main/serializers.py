from rest_framework import serializers
from .models import (
    WebDeveloperSalary, 
    JobVacancyShare, 
    CybersecuritySalary,
    Home,
    Demand,
    Skills,
    Geography
)

class WebDeveloperSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = WebDeveloperSalary
        fields = '__all__'

class JobVacancyShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobVacancyShare
        fields = '__all__'

class CybersecuritySalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CybersecuritySalary
        fields = '__all__'

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class GeographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography
        fields = '__all__'
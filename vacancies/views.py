import requests
from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect

def fetch_vacancies(request):
    return HttpResponseRedirect("https://hh.ru/search/vacancy?text=IT")

def fetch_vacancies(request):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": "IT",  
        "period": 1,  
        "per_page": 10,  
        "order_by": "publication_time",  
    }
    response = requests.get(url, params=params)
    data = response.json()

    vacancies = []
    for item in data.get("items", []):
        vacancy_id = item.get("id")
        vacancy_details = requests.get(f"https://api.hh.ru/vacancies/{vacancy_id}").json()

        vacancy = {
            "title": item.get("name"),
            "description": vacancy_details.get("description", ""),
            "skills": ", ".join(skill.get("name") for skill in vacancy_details.get("key_skills", [])),
            "company": item.get("employer", {}).get("name", ""),
            "salary": item.get("salary", {}).get("from", "") if item.get("salary") else "Не указано",
            "region": item.get("area", {}).get("name", ""),
            "published_date": datetime.strptime(item.get("published_at"), "%Y-%m-%dT%H:%M:%S%z").strftime("%d.%m.%Y %H:%M"),
            "url": item.get("alternate_url", "#"),  
        }
        vacancies.append(vacancy)

    return render(request, 'vacancies/vacancy_list.html', {'vacancies': vacancies})
    
from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название вакансии")
    description = models.TextField(verbose_name="Описание вакансии")
    skills = models.CharField(max_length=255, verbose_name="Навыки")
    company = models.CharField(max_length=255, verbose_name="Компания")
    salary = models.CharField(max_length=100, verbose_name="Оклад")
    region = models.CharField(max_length=100, verbose_name="Регион")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
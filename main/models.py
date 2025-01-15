from django.db import models

class Home(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='homepage')
    text_1 = models.TextField('Текст 1', default='')
    text_2 = models.TextField('Текст 2', default='')
    image_1 = models.ImageField('img 1', default='default_image.png', upload_to='home')
    image_2 = models.ImageField('img 2', default='default_image.png', upload_to='home')

    def __str__(self):
        return self.title

class Demand(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='demand')
    text = models.TextField('Текст', blank=True, null=True)
    graph_left = models.ImageField('График №2', upload_to='demand', blank=True, null=True)
    graph_right = models.ImageField('График №1', upload_to='demand', blank=True, null=True)

    def __str__(self):
        return self.title

class Geography(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='География')
    text = models.TextField('Текст', blank=True, null=True)
    salary_table = models.TextField('Таблица зарплат', blank=True, null=True)  # جدول الرواتب
    vacancy_table = models.TextField('Таблица вакансий', blank=True, null=True)  # جدول الوظائف
    graph = models.ImageField('График', upload_to='geography', blank=True, null=True)

    def __str__(self):
        return self.title

class WebDeveloperSalary(models.Model):
    city = models.CharField(max_length=100, verbose_name="Город")
    average_salary = models.CharField(max_length=100, verbose_name="Средняя зарплата")
    notes = models.TextField(verbose_name="Примечания")

    def __str__(self):
        return self.city

class JobVacancyShare(models.Model):
    city = models.CharField(max_length=100, verbose_name="Город")
    share = models.CharField(max_length=10, verbose_name="Доля вакансий")
    notes = models.TextField(verbose_name="Примечания")

    def __str__(self):
        return self.city

class CybersecuritySalary(models.Model):
    city = models.CharField(max_length=100, verbose_name="Город")
    average_salary = models.CharField(max_length=100, verbose_name="Средняя зарплата")
    notes = models.TextField(verbose_name="Примечания")

    def __str__(self):
        return self.city

class Skills(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='skills')
    text = models.TextField('Текст', blank=True, null=True)
    graph = models.ImageField('График', upload_to='skills', blank=True, null=True)

    def __str__(self):
        return self.title

class Statistics(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='Общая статистика')
    salary_trend_graph = models.ImageField('График динамики уровня зарплат', upload_to='statistics', blank=True, null=True)
    vacancy_trend_graph = models.ImageField('График динамики количества вакансий', upload_to='statistics', blank=True, null=True)
    salary_city_table = models.TextField('Таблица уровня зарплат по городам', blank=True, null=True)
    vacancy_share_city_table = models.TextField('Таблица доли вакансий по городам', blank=True, null=True)
    top_skills_table = models.TextField('ТОП-20 навыков по годам', blank=True, null=True)

    def __str__(self):
        return self.title



        
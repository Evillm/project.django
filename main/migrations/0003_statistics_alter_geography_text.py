# Generated by Django 4.2.17 on 2025-01-14 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_skills_graph'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Общая статистика', max_length=100, verbose_name='Заголовок')),
                ('salary_trend_graph', models.ImageField(default=None, upload_to='statistics', verbose_name='График динамики уровня зарплат')),
                ('vacancy_trend_graph', models.ImageField(default=None, upload_to='statistics', verbose_name='График динамики количества вакансий')),
                ('salary_city_table', models.TextField(default=None, verbose_name='Таблица уровня зарплат по городам')),
                ('vacancy_share_city_table', models.TextField(default=None, verbose_name='Таблица доли вакансий по городам')),
                ('top_skills_table', models.TextField(default=None, verbose_name='ТОП-20 навыков по годам')),
            ],
        ),
        migrations.AlterField(
            model_name='geography',
            name='text',
            field=models.TextField(default=None, verbose_name='Текст'),
        ),
    ]

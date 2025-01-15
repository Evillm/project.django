# Generated by Django 4.2.17 on 2025-01-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_statistics_alter_geography_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='CybersecuritySalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('average_salary', models.CharField(max_length=100, verbose_name='Средняя зарплата')),
                ('notes', models.TextField(verbose_name='Примечания')),
            ],
        ),
        migrations.CreateModel(
            name='JobVacancyShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('share', models.CharField(max_length=10, verbose_name='Доля вакансий')),
                ('notes', models.TextField(verbose_name='Примечания')),
            ],
        ),
        migrations.CreateModel(
            name='WebDeveloperSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('average_salary', models.CharField(max_length=100, verbose_name='Средняя зарплата')),
                ('notes', models.TextField(verbose_name='Примечания')),
            ],
        ),
        migrations.RemoveField(
            model_name='geography',
            name='graph',
        ),
        migrations.RemoveField(
            model_name='geography',
            name='table',
        ),
        migrations.RemoveField(
            model_name='geography',
            name='text',
        ),
        migrations.RemoveField(
            model_name='geography',
            name='title',
        ),
        migrations.AddField(
            model_name='geography',
            name='average_salary',
            field=models.CharField(default='N/A', max_length=100, verbose_name='Средняя зарплата'),
        ),
        migrations.AddField(
            model_name='geography',
            name='city',
            field=models.CharField(default=0, max_length=100, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='geography',
            name='notes',
            field=models.TextField(default='N/A', verbose_name='Примечания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='demand',
            name='graph_left',
            field=models.ImageField(blank=True, null=True, upload_to='demand', verbose_name='График №2'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='graph_right',
            field=models.ImageField(blank=True, null=True, upload_to='demand', verbose_name='График №1'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='home',
            name='image_1',
            field=models.ImageField(default='default_image.png', upload_to='home', verbose_name='img 1'),
        ),
        migrations.AlterField(
            model_name='home',
            name='image_2',
            field=models.ImageField(default='default_image.png', upload_to='home', verbose_name='img 2'),
        ),
        migrations.AlterField(
            model_name='home',
            name='text_1',
            field=models.TextField(default='', verbose_name='Текст 1'),
        ),
        migrations.AlterField(
            model_name='home',
            name='text_2',
            field=models.TextField(default='', verbose_name='Текст 2'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='graph',
            field=models.ImageField(blank=True, null=True, upload_to='skills', verbose_name='График'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='salary_city_table',
            field=models.TextField(blank=True, null=True, verbose_name='Таблица уровня зарплат по городам'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='salary_trend_graph',
            field=models.ImageField(blank=True, null=True, upload_to='statistics', verbose_name='График динамики уровня зарплат'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='top_skills_table',
            field=models.TextField(blank=True, null=True, verbose_name='ТОП-20 навыков по годам'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='vacancy_share_city_table',
            field=models.TextField(blank=True, null=True, verbose_name='Таблица доли вакансий по городам'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='vacancy_trend_graph',
            field=models.ImageField(blank=True, null=True, upload_to='statistics', verbose_name='График динамики количества вакансий'),
        ),
    ]

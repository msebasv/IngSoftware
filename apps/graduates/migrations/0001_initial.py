# Generated by Django 4.2.1 on 2023-06-02 00:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=250, verbose_name='Position')),
                ('sector', models.CharField(max_length=250, verbose_name='Sector')),
                ('company', models.CharField(max_length=250, verbose_name='Company')),
                ('type', models.CharField(max_length=250, verbose_name='Type')),
            ],
            options={
                'db_table': 'Job',
            },
        ),
        migrations.CreateModel(
            name='Graduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_range', models.CharField(choices=[('1', '1.000.000 - 3.000.0000'), ('2', '3.000.000 - 6.000.000'), ('3', '6.000.000 - 9.000.000'), ('4', '9.000.000 - 12.000.000'), ('5', '12.000.000 - 15.000.000'), ('6', '15.000.000 - En adelante')], max_length=250, null=True, verbose_name='Salary Range')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('previous_email', models.EmailField(max_length=254, verbose_name='Previous Email')),
                ('achievement_level', models.CharField(max_length=250, null=True, verbose_name='Achievement Level')),
                ('work_experience', models.PositiveSmallIntegerField(null=True, verbose_name='Work Experience')),
                ('cv', models.FileField(upload_to='cv/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='CV')),
                ('job_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='graduates.job')),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'db_table': 'Graduate',
            },
        ),
    ]

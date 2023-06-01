# Generated by Django 4.2.1 on 2023-06-01 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('category', models.CharField(max_length=250, verbose_name='Category')),
                ('required', models.BooleanField(verbose_name='Required')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'db_table': 'Question',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField(verbose_name='Salary')),
                ('faculty', models.CharField(max_length=250, verbose_name='Faculty')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='Teacher_Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('schedule', models.CharField(max_length=250, verbose_name='Schedule')),
                ('classroom', models.CharField(max_length=250, verbose_name='Classroom')),
                ('status', models.BooleanField(default='Active', max_length=250, verbose_name='Status')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
            options={
                'db_table': 'Teacher_Subject',
            },
        ),
        migrations.CreateModel(
            name='Evaluation_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=250, verbose_name='Semester')),
                ('score', models.PositiveSmallIntegerField(verbose_name='Score')),
                ('type', models.CharField(max_length=250, verbose_name='Type')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
            options={
                'db_table': 'Evaluation_History',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('type', models.CharField(max_length=250, verbose_name='Type')),
                ('grade', models.PositiveSmallIntegerField(verbose_name='Grade')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.question')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
            options={
                'db_table': 'Evaluation',
            },
        ),
    ]
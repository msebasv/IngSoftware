# Generated by Django 4.2.1 on 2023-06-03 17:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0002_remove_job_position_graduate_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='achievement_level',
            field=models.CharField(default='Sin asignar', max_length=250, verbose_name='Achievement Level'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='cv',
            field=models.FileField(default='Sin asignar', upload_to='cv/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='CV'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='email',
            field=models.EmailField(default='Sin asignar', max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='position',
            field=models.CharField(default='Sin asignar', max_length=250, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='salary_range',
            field=models.CharField(choices=[('1', '1.000.000 - 3.000.0000'), ('2', '3.000.000 - 6.000.000'), ('3', '6.000.000 - 9.000.000'), ('4', '9.000.000 - 12.000.000'), ('5', '12.000.000 - 15.000.000'), ('6', '15.000.000 - En adelante')], default='Sin asignar', max_length=250, verbose_name='Salary Range'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='work_experience',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Work Experience'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(default='Sin asignar', max_length=250, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='job',
            name='sector',
            field=models.CharField(default='Sin asignar', max_length=250, verbose_name='Sector'),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(default='Sin asignar', max_length=250, verbose_name='Type'),
        ),
    ]
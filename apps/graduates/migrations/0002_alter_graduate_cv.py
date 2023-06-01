# Generated by Django 4.1.5 on 2023-06-01 23:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='cv',
            field=models.FileField(upload_to='cv/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='CV'),
        ),
    ]

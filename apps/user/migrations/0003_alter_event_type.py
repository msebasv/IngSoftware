# Generated by Django 4.1.5 on 2023-06-03 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_event_date_remove_event_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.IntegerField(choices=[(1, 'Tipo 1'), (2, 'Tipo 2'), (3, 'Tipo 3')], verbose_name='Type'),
        ),
    ]

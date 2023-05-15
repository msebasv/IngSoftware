# Generated by Django 4.1.5 on 2023-05-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Usuario')),
                ('email', models.CharField(max_length=254, unique=True, verbose_name='Correo')),
                ('name', models.CharField(blank=True, max_length=254, null=True, verbose_name='Nombres')),
                ('lastname', models.CharField(blank=True, max_length=254, null=True, verbose_name='Apellidos')),
                ('active_user', models.BooleanField(default=True)),
                ('admin_user', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

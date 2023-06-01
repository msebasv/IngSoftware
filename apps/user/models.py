from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from datetime import date


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, name, lastname, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")

        user = self.model(username=username, email=self.normalize_email(email), name=name, lastname=lastname)
        user.password = password
        user.save()
        return user

    def create_superuser(self, username, name, lastname, email, password, **extra_fields):
        user = self.create_user(username=username, name=name, lastname=lastname, email=email)
        user.password = password
        user.admin_user = True
        user.save()
        return user
    
class User(AbstractBaseUser):
    username = models.CharField("Usuario", unique=True, max_length=100)
    previous_user = models.CharField(max_length=250, null=True, blank=True, unique=True, verbose_name="Previous User")
    email = models.CharField("Correo", unique=True, max_length=254)
    previous_email = models.EmailField(null=True)
    name = models.CharField("Nombres", max_length=254, blank=True, null=False)
    lastname = models.CharField("Apellidos", max_length=254, blank=True, null=True)
    phone = models.CharField("Telefono",max_length=250, null=True)
    DEFAULT_BIRTHDAY = date(2000, 1, 1)
    
    birthday = models.DateField("Fecha de Nacimiento", null=True, default=DEFAULT_BIRTHDAY)
    address = models.CharField("Dirección",max_length=250, null=False)
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    gender = models.CharField("Género", max_length=1, choices=GENDER_CHOICES, default='F')
    active_user = models.BooleanField("Usuario Activo",default=True)
    admin_user = models.BooleanField("Usuario Administrador",default=False)
    objects = UserManager()
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'lastname']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin_user
    class Meta:
        db_table = 'User'

class Event(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, null=False, verbose_name="Event Date")
    time = models.TimeField(auto_now=False, auto_now_add=False, null=False, verbose_name="Event Time")
    type = models.CharField(max_length=250, null=False, verbose_name="Type")
    description = models.CharField(max_length=250, null=False, verbose_name="Description")
    subject = models.CharField(max_length=250, null=False, verbose_name="Subject")
    status = models.BooleanField(null=False, default=True, verbose_name="Status")
    class Meta:
        db_table = 'Event'

class Event_User(models.Model):
    id_user=models.ForeignKey(User,on_delete=models.CASCADE, null=False, blank=False)
    id_Event=models.ForeignKey(Event,on_delete=models.CASCADE, null=False, blank=False)
    permissions=models.CharField(max_length=250, null=False, verbose_name="permissions")
    class Meta:
        db_table = 'Event_User'
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, name, lastname, password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")

        user = self.model(username=username, email=self.normalize_email(
            email), name=name, lastname=lastname)

        user.set_password(password)
        print("HOLA")
        print(user.password)
        user.save()
        return user

    def create_superuser(self, email, username, name, lastname, password=None):
        user = self.create_user(email,
                                username=username, name=name, lastname=lastname,
                                password=password
                                )
        user.admin_user = True
        user.save()
        return user


class User(AbstractBaseUser):
    username = models.CharField("Usuario", unique=True, max_length=100)
    email = models.CharField("Correo", unique=True, max_length=254)
    name = models.CharField("Nombres", max_length=254, blank=True, null=True)
    lastname = models.CharField(
        "Apellidos", max_length=254, blank=True, null=True)
    active_user = models.BooleanField(default=True)
    admin_user = models.BooleanField(default=False)
    objects = UserManager()

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

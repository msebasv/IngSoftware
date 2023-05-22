from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,name, lastname, phone_Number,username,email,birthday,address,password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")

        user = self.model(name=name,lastname=lastname,phone_Number=phone_Number,username=username,birthday=birthday,address=address, email=self.normalize_email(
            email))

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,name, lastname,usernameclear,email,password=None):

        user = self.model(name=name,lastname=lastname,phone_Number=None,username=username,birthday=None,address=None, email=self.normalize_email(
            email), password=password)
        user.admin_user = True
        user.save()
        return user


class User(AbstractBaseUser):
    name = models.CharField("Nombres", max_length=254, blank=True, null=False)
    lastname = models.CharField("Apellidos", max_length=254, blank=True, null=True)
    phone_Number = models.CharField("Telefono", max_length=7, blank=True, null=True)
    username = models.CharField("Usuario", unique=True, max_length=100, null=False)
    previous_Username = models.CharField("Usuario anterior", unique=True, max_length=100, null=True)
    email = models.CharField("Correo", unique=True, max_length=254)
    previous_Email = models.CharField("Correo Anterior", unique=True, max_length=254, null=True)
    birthday = models.DateField("Nacimiento", null=True)
    address = models.CharField("Dirección", max_length=254, null=True)
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

class estudent(models.Model):
    id_Estudent = models.IntegerField(primary_key=True)
    semester = models.PositiveSmallIntegerField()
    career = models.CharField(max_length=50)
    id_User = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        verbose_name='Estudiante'
        verbose_name_plural="Estudiantes"
        db_table='estudent'

class administrative(models.Model):
    id_administrative = models.IntegerField(primary_key=True)
    salary = models.FloatField()
    position = models.CharField(max_length=50)
    id_User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
    class Meta:
        verbose_name='Administrador'
        verbose_name_plural="Administradores"
        db_table='administrative'

class teacher(models.Model):
    id_teacher = models.IntegerField(primary_key=True)
    Salary = models.FloatField()
    Faculty = models.CharField(max_length=50)
    Id_User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
    class Meta:
        verbose_name='Profesor'
        verbose_name_plural="Profesores"
        db_table='teacher'

class employment(models.Model):
    id_employment = models.IntegerField(primary_key=True)
    position= models.CharField(max_length=100)
    Sector = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return super().__str__()
    class Meta:
        verbose_name='Empleo'
        verbose_name_plural="Empleos"
        db_table='employment'

class graduated(models.Model):
    id_graduated = models.IntegerField(primary_key=True)
    salary_Range = models.IntegerField()
    title = models.CharField(max_length=50)
    email_act = models.CharField(max_length=100)
    previous_email = models.CharField(max_length=100)
    level_Reached = models.CharField(max_length=100)
    work_experience = models.PositiveSmallIntegerField()
    cv = models.BinaryField()
    id_Estudent = models.ForeignKey(estudent, on_delete=models.CASCADE)
    id_employment = models.ForeignKey(employment, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
    class Meta:
        verbose_name='Egresado'
        verbose_name_plural="Egresados"
        db_table='graduated'
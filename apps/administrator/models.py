from django.db import models
from django.core.validators import FileExtensionValidator
from apps.user.models import User


# Create your models here.

class Administrative(models.Model):
    salary = models.FloatField(verbose_name="Salary")
    position = models.CharField(max_length=250, null=False, verbose_name="Position")
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Administrative'
    

class Comite (models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="Name")
    type = models.CharField(max_length=50, null=False, verbose_name="Type")
    description = models.CharField(max_length=250, null=False, verbose_name="Description")
    status = models.BooleanField(default=True,verbose_name="Status")
    class Meta:
        db_table = 'Comite'

class Act (models.Model):
    title = models.CharField(max_length=250, null=False, verbose_name="Titulo")
    type = models.CharField(max_length=250, null=False, verbose_name="Tipo")
    description =  models.CharField(max_length=250, null=False, verbose_name="Descripcion")
    date_actual = models.DateField(auto_now=False, auto_now_add=False, null=False, verbose_name="Fecha Actual")
    date_modify = models.DateField(auto_now=False, auto_now_add=False,null=False,verbose_name="Fecha Modificacion")
    document = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])],null=True,verbose_name="Document")
    state = models.BooleanField(default=True)
    id_comite = models.ForeignKey(Comite, on_delete= models.CASCADE, null=False, blank=False)
    id_administrative = models.ForeignKey(Administrative, on_delete= models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Act'


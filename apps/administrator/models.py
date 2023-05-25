from django.db import models
from apps.user.models import Administrative

# Create your models here.
class Act (models.Model):
    title = models.CharField(max_length=250, null=False, verbose_name="Titulo")
    type = models.CharField(max_length=250, null=False, verbose_name="Tipo")
    description =  models.CharField(max_length=250, null=False, verbose_name="Descripcion")
    date_actual = models.DateField(auto_now=False, auto_now_add=False, null=False, verbose_name="Fecha Actual")
    date_modify = models.DateField(auto_now=False, auto_now_add=False,null=False,verbose_name="Fecha Modificacion")
    state = models.CharField(max_length=250, null=False, verbose_name="Estado")
    id_administrative = models.ForeignKey(Administrative, on_delete= models.CASCADE, null=False, blank=False)
from django.db import models
from django.core.validators import FileExtensionValidator
from apps.user.models import Administrative

# Create your models here.

class Act(models.Model):
    title = models.CharField(max_length=250, null=False, verbose_name="Title")
    type = models.CharField(max_length=250, null=False, verbose_name="Type")
    description = models.CharField(max_length=250, null=False, verbose_name="Description")
    current_date = models.DateField(auto_now=False, auto_now_add=False, null=False, verbose_name="Current Date")
    modification_date = models.DateField(auto_now=False, auto_now_add=False, null=False, verbose_name="Modification Date")
    document = models.FileField(validators=[FileExtensionValidator(['pdf'])], verbose_name="Document")
    status = models.CharField(max_length=250, null=False, verbose_name="Status", default="Active")
    administrative_id = models.ForeignKey(Administrative, on_delete=models.CASCADE, null=False, blank=False)
    
    class Meta:
        db_table = 'Acts'
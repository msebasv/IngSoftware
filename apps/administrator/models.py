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


class Committee (models.Model):
    name = models.CharField(max_length=250, null=False, verbose_name="Name")    
    class Meta:
        db_table = "Committee"
        
    def __str__(self):
        return self.name


class ActType(models.Model):
    name = models.CharField(max_length=250, null=False, verbose_name="Name")
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "ActTypes"

    def __str__(self):
        return self.name


class Act(models.Model):
    title = models.CharField(max_length=250, null=False, verbose_name="Title")
    type = models.ForeignKey(ActType, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Type")
    description = models.CharField(max_length=250, null=False, verbose_name="Description")
    current_date = models.DateField(auto_now=False, auto_now_add=True, null=False, verbose_name="Current Date")
    modification_date = models.DateField(auto_now=False, auto_now_add=True, null=False, verbose_name="Modification Date")
    document = models.FileField(upload_to="filesAct/",validators=[FileExtensionValidator(['pdf'])], verbose_name="Document", null=True)
    status = models.BooleanField(verbose_name="Status", default=True)
    administrative_id = models.ForeignKey(Administrative, on_delete=models.CASCADE, null=True, blank=True)
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = 'Acts'
        
    def __str__(self):
        return self.title
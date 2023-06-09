from django.db import models
from django.core.validators import FileExtensionValidator
from apps.student.models import Student
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Job(models.Model):
    sector = models.CharField(default='Sin asignar',max_length=250, null=True, verbose_name="Sector")
    company = models.CharField(default='Sin asignar',max_length=250, null=True, verbose_name="Company")
    type = models.CharField(default='Sin asignar',max_length=250, null=True, verbose_name="Type")
    class Meta:
        db_table = 'Job'

class Graduate(models.Model):
    position = models.CharField(default='Sin asignar',max_length=250, null=False, verbose_name="Position")
    SALARY_CHOICES = [
        ('1', '1.000.000 - 3.000.0000'),
        ('2', '3.000.000 - 6.000.000'),
        ('3', '6.000.000 - 9.000.000'),
        ('4', '9.000.000 - 12.000.000'),
        ('5', '12.000.000 - 15.000.000'),
        ('6', '15.000.000 - En adelante')
    ]
    salary_range = models.CharField(default='Sin asignar',max_length=250, null=False, verbose_name="Salary Range", choices=SALARY_CHOICES)
    email = models.EmailField(default='Sin asignar',verbose_name="Email")
    previous_email = models.EmailField(verbose_name="Previous Email")
    achievement_level = models.CharField(default='Sin asignar',max_length=250, null=False, verbose_name="Achievement Level")
    work_experience = models.PositiveSmallIntegerField(default= 0, null=False, verbose_name="Work Experience")
    cv = models.FileField(default='Sin asignar', null= False,upload_to="cv/", validators=[FileExtensionValidator(['pdf'])], verbose_name="CV")
    job_id = models.OneToOneField(Job, on_delete=models.CASCADE, null=True, blank=False)
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Graduate'

@receiver(post_save, sender=Graduate)
def create_job(sender, instance, created, **kwargs):
    if created:
        job = Job.objects.create()
        instance.job_id = job
        instance.save()
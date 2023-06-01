from django.db import models
from django.core.validators import FileExtensionValidator
from apps.student.models import Student
# Create your models here.
class Job(models.Model):
    position = models.CharField(max_length=250, null=False, verbose_name="Position")
    sector = models.CharField(max_length=250, null=False, verbose_name="Sector")
    company = models.CharField(max_length=250, null=False, verbose_name="Company")
    type = models.CharField(max_length=250, null=False, verbose_name="Type")
    class Meta:
        db_table = 'Job'

class Graduate(models.Model):
    salary_range = models.CharField(max_length=250, null=True, verbose_name="Salary Range")
    email = models.EmailField(verbose_name="Email")
    previous_email = models.EmailField(verbose_name="Previous Email")
    achievement_level = models.CharField(max_length=250, null=True, verbose_name="Achievement Level")
    work_experience = models.PositiveSmallIntegerField(null=True, verbose_name="Work Experience")
    cv = models.FileField(validators=[FileExtensionValidator(['pdf'])], verbose_name="CV")
    job_id = models.OneToOneField(Job, on_delete=models.CASCADE, null=True, blank=False)
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Graduate'
from django.db import models
<<<<<<< HEAD
from apps.user.models import User
=======
from apps.user.models import User_General
>>>>>>> 944f203429d9e85b419c11df60451f28341062dc

# Create your models here.
class Student(models.Model):
    semester = models.PositiveSmallIntegerField(verbose_name="Semester")
    major = models.CharField(max_length=250, null=False, verbose_name="Major")
<<<<<<< HEAD
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
=======
    user_id = models.OneToOneField(User_General, on_delete=models.CASCADE, null=False, blank=False)
>>>>>>> 944f203429d9e85b419c11df60451f28341062dc
    class Meta:
        db_table = 'Student'

class Enrollment(models.Model):
    cost = models.CharField(max_length=7, null=False, blank=False, verbose_name="Cost")
    academic_period = models.CharField(max_length=10, null=False, blank=False, verbose_name="Academic Period")
    credit_count = models.PositiveSmallIntegerField(verbose_name="Credit Count")
    status = models.BooleanField(max_length=10, default=True, verbose_name="Status")
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Enrollment'

class Student_Subject(models.Model):
    name = models.CharField(max_length=250, null=False, verbose_name="Name")
    shift = models.CharField(max_length=250, null=False, verbose_name="Shift")
    schedule = models.CharField(max_length=250, null=False, verbose_name="Schedule")
    class Meta:
        db_table = 'Student_Subject'

class Subject_Enrollment(models.Model):
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE, null=False, blank=False)
    subject_id = models.ForeignKey(Student_Subject, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Subject_Enrollment'
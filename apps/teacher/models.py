from django.db import models

from apps.user.models import User


# Create your models here.
class Teacher(models.Model):
    salary = models.FloatField(verbose_name="Salary")
    faculty = models.CharField(max_length=250, null=False, verbose_name="Faculty")

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'Teacher'
class Evaluation_History(models.Model):
    semester = models.CharField(max_length=250, null=False, verbose_name="Semester")
    score = models.PositiveSmallIntegerField(verbose_name="Score")
    type = models.CharField(max_length=250, null=False, verbose_name="Type")
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Evaluation_History'
class Teacher_Subject(models.Model):
    name = models.CharField(max_length=250, null=False, verbose_name="Name")
    description = models.CharField(max_length=250, null=False, verbose_name="Description")
    schedule = models.CharField(max_length=250, null=False, verbose_name="Schedule")
    classroom = models.CharField(max_length=250, null=False, verbose_name="Classroom")
    status = models.BooleanField(max_length=250, null=False, default="Active", verbose_name="Status")
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Teacher_Subject'

class Question(models.Model):
    title = models.CharField(max_length=250, null=False, verbose_name="Title")
    category = models.CharField(max_length=250, null=False, verbose_name="Category")
    required = models.BooleanField(verbose_name="Required")
    status = models.BooleanField(null=False, default=True, verbose_name="Status")
    class Meta:
        db_table = 'Question'

class Evaluation(models.Model):
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=False, verbose_name="Start Date")
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=False, verbose_name="End Date")
    type = models.CharField(max_length=250, null=False, verbose_name="Type")
    grade = models.PositiveSmallIntegerField(verbose_name="Grade")
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, blank=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Evaluation'
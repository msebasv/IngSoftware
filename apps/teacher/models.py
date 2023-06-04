from django.db import models
from django.utils import timezone
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
class Subject(models.Model):
    name = models.CharField(max_length=250, null=False, verbose_name="Name")
    description = models.CharField(max_length=250, null=False, verbose_name="Description")
    schedule = models.CharField(max_length=250, null=False, verbose_name="Schedule")
    classroom = models.CharField(max_length=250, null=False, verbose_name="Classroom")
    status = models.BooleanField(max_length=250, null=False, default="Active", verbose_name="Status")

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Subject'

class Question(models.Model):
    title = models.CharField(max_length=250, null=False, verbose_name="Title")
    category = models.CharField(max_length=250, null=False, verbose_name="Category")
    required = models.BooleanField(verbose_name="Required")
    status = models.BooleanField(null=False, default=True, verbose_name="Status")
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Question'

class Evaluation(models.Model):
    date = models.DateField(default=timezone.now, auto_now_add=False, null=False, verbose_name="Date")
    type = models.CharField(default='Temprana',max_length=250, null=False, verbose_name="Type")
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, blank=False)
    Subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Evaluation'

class Preg_Ev(models.Model):
    EVALUATION_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    id_evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, null=False, blank=False)
    grade = models.PositiveSmallIntegerField(choices=EVALUATION_CHOICES)
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'Preg_Ev'
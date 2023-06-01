from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import FileExtensionValidator

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, name, lastname, password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")

        user = self.model(username=username, email=self.normalize_email(
            email), name=name, lastname=lastname)

        user.set_password(password)
        print("HOLA")
        print(user.password)
        user.save()
        return user

    def create_superuser(self, email, username, name, lastname, password=None):
        user = self.create_user(email,
                                username=username, name=name, lastname=lastname,
                                password=password
                                )
        user.admin_user = True
        user.save()
        return user
    
class User(AbstractBaseUser):
    username = models.CharField("Usuario", unique=True, max_length=100)
    email = models.CharField("Correo", unique=True, max_length=254)
    name = models.CharField("Nombres", max_length=254, blank=True, null=True)
    lastname = models.CharField(
        "Apellidos", max_length=254, blank=True, null=True)
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
    class Meta:
        db_table = 'Super_User'
    
class User_General(models.Model):
    #id_usuario = models.IntegerField(primary_key=True, verbose_name="User Identification")
    name = models.CharField(max_length=250, null=False,blank=False, verbose_name="Name")
    last_name = models.CharField(max_length=250, null=False,blank=False, verbose_name="Last Name")
    phone = models.CharField(max_length=250, null=True, verbose_name="Phone")
    institutional_user = models.CharField(max_length=250, null=False,blank=False,unique=True,verbose_name="Institutional User")
    previous_user = models.CharField(max_length=250, null=True,blank=True,unique=True,verbose_name="Previous User")
    email = models.EmailField(verbose_name="Email")
    previous_email = models.EmailField(verbose_name="Previous Email")
    password = models.CharField(max_length=50, null=False, verbose_name="Password")
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=False, verbose_name="Date of Birth")
    address = models.CharField(max_length=250, null=False, verbose_name="Address")
    status = models.CharField(max_length=250, null=False, verbose_name="Status")
    class Meta:
        db_table = 'User'

class Student(models.Model):
    semester = models.PositiveSmallIntegerField(verbose_name="Semester")
    major = models.CharField(max_length=250, null=False, verbose_name="Major")
    user_id = models.OneToOneField(User_General, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Student'

class Enrollment(models.Model):
    cost = models.CharField(max_length=7, null=False, blank=False, verbose_name="Cost")
    academic_period = models.CharField(max_length=10, null=False, blank=False, verbose_name="Academic Period")
    credit_count = models.PositiveSmallIntegerField(verbose_name="Credit Count")
    status = models.CharField(max_length=10, default="Active", verbose_name="Status")
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

class Event(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, null=False, verbose_name="Event Date")
    time = models.TimeField(auto_now=False, auto_now_add=False, null=False, verbose_name="Event Time")
    type = models.CharField(max_length=250, null=False, verbose_name="Type")
    description = models.CharField(max_length=250, null=False, verbose_name="Description")
    subject = models.CharField(max_length=250, null=False, verbose_name="Subject")
    status = models.CharField(max_length=250, null=False, default="Active", verbose_name="Status")
    class Meta:
        db_table = 'Event'

class Event_User(models.Model):
    id_user=models.ForeignKey(User_General,on_delete=models.CASCADE, null=False, blank=False)
    id_Event=models.ForeignKey(Event,on_delete=models.CASCADE, null=False, blank=False)
    permissions=models.CharField(max_length=250, null=False, verbose_name="permissions")
    class Meta:
        db_table = 'Event_User'

class Administrative(models.Model):
    salary = models.FloatField(verbose_name="Salary")
    position = models.CharField(max_length=250, null=False, verbose_name="Position")
    user_id = models.OneToOneField(User_General, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Administrative'

class Teacher(models.Model):
    salary = models.FloatField(verbose_name="Salary")
    faculty = models.CharField(max_length=250, null=False, verbose_name="Faculty")
    user_id = models.OneToOneField(User_General, on_delete=models.CASCADE, null=False, blank=False)
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
    status = models.CharField(max_length=250, null=False, default="Active", verbose_name="Status")
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'Teacher_Subject'

class Question(models.Model):
    title = models.CharField(max_length=250, null=False, verbose_name="Title")
    category = models.CharField(max_length=250, null=False, verbose_name="Category")
    required = models.BooleanField(verbose_name="Required")
    status = models.CharField(max_length=250, null=False, default="Active", verbose_name="Status")
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
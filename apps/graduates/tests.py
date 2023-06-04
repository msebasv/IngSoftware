from django.test import TestCase
from apps.student.models import Student
from .models import graduates

class GraduateModelTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name="John Doe", age=25)
        self.graduates = graduates.objects.create(
            salary_range='1',
            email='john@example.com',
            previous_email='previous@example.com',
            achievement_level='High',
            work_experience=3,
            cv='cv/example.pdf',
            job_id=None,
            student_id=self.student
        )

    def test_model_fields(self):
        self.assertEqual(self.graduates.salary_range, '1')
        self.assertEqual(self.graduates.email, 'john@example.com')
        self.assertEqual(self.graduates.previous_email, 'previous@example.com')
        self.assertEqual(self.graduates.achievement_level, 'High')
        self.assertEqual(self.graduates.work_experience, 3)
        self.assertEqual(self.graduates.cv, 'cv/example.pdf')
        self.assertIsNone(self.graduates.job_id)
        self.assertEqual(self.graduates.student_id, self.student)

    def test_model_table_name(self):
        self.assertEqual(self.graduates._meta.db_table, 'Graduate')
from django.test import TestCase
from.factories import StudentFactory
from ..models import Student

class StudentTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        student = StudentFactory()
        self.assertEqual(str(student), student.first_name)

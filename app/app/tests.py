"""Sample tests"""

from django.test import SimpleTestCase
from app import calc 

class CalcTests(SimpleTestCase):
    """test the calc module"""
    def test_add_numbers(self):
        """test adding add function"""
        res=calc.add(3,5)
        self.assertEqual(res,8)
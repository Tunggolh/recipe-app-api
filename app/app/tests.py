"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(20, 5)

        self.assertEqual(res, 25)

    def test_substract_numbers(self):
        """Test ubstracting numbers."""
        res = calc.substract(10, 15)

        self.assertEqual(res, 5)

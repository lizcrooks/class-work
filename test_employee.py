import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""
    
    def setUp(self):
        """Make an employee to use in tests."""
        self.james = Employee('james', 'mensch', 112000)

    def test_give_default_raise(self):
        """Test that a default raise works out."""
        self.james.give_raise()
        self.assertEqual(self.james.salary, 117000)

    def test_give_custom_raise(self):
        """Test that a custom raise works the way it should."""
        self.james.give_raise(20000)
        self.assertEqual(self.james.salary, 132000)

unittest.main()
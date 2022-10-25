import unittest
import datetime

from util import age

class TestUtil(unittest.TestCase):

    def test_age(self):

        class MockDatetime(datetime.datetime):
            @classmethod
            def today(cls):
                return cls(2022, 8, 22)
        datetime.datetime = MockDatetime

        self.assertEqual(datetime.datetime.today().year, 2022)
        self.assertEqual(age("15.01.1998"), 24)


if __name__ == '__main__':
    unittest.main()
__project__ = "hellofortika"
import unittest
from unittest import TestCase

from hellofortika.classes.hellofortika import HelloFortika


class TestHelloFortika(TestCase):

    def test_print(self):
        hf = HelloFortika()
        ret = hf.print_fortika()
        self.assertEqual(ret, 0)


if __name__ == '__main__':
    unittest.main()

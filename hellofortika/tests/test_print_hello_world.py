__project__="hellofortika"
import unittest
from unittest import TestCase

from hellofortika.lib.libhellofortika import print_hello_world

class TestPrint_hello_world(TestCase):

    def test_print_hello_world(self):
        res=print_hello_world()
        self.assertEqual(res,0)

if __name__ == '__main__':
    unittest.main()

 from __future__ import print_function
from msilib.schema import tables
 import unittest
 class TestFoo(unittest.TestCase):
     def test_foo(self):
             self.assertTrue(True)
     def fun_not_run(self):
             print("no run")

 unittest.main()
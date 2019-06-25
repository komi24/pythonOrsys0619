# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:17:50 2019

@author: miguel
"""
import unittest
from .module1 import multiplier


class TestMultiplier(unittest.TestCase):
    def setUp(self):
        self.a = 2
        self.b = 4
    def testMultiplication(self):
        self.assertEqual(8, multiplier(self.a, self.b))
    
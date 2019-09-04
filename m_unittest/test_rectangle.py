# -*- coding: utf-8 -*-
from unittest import TestCase
from test.unittest.geometry import Rectangle

__author__ = 'JiaweiMao'
__version__ = '1.0.0'


class TestRectangle(TestCase):
    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

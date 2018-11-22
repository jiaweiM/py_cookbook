# -*- coding: utf-8 -*-

__author__ = 'JiaweiMao'
__version__ = '1.0.0'


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# -*- coding: utf-8 -*-

__author__ = 'JiaweiMao'
__version__ = '1.0.0'


class TestClass(object):
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')

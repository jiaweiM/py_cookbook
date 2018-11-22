# -*- coding: utf-8 -*-
import pytest_test

__author__ = 'JiaweiMao'
__version__ = '1.0.0'


class TestSample:
    @pytest_test.fixture()
    def count(self):
        print('init count')
        return 10

    def test_answer2(self, count):
        print('get count %s', count)
        assert count == 10

    def test_answer(self):
        print('this is a log')
        assert 1 + 2 == 3

# -*- coding: utf-8 -*-

import pytest_test

__author__ = 'JiaweiMao'
__version__ = '1.0.0'


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest_test.raises(SystemExit):
        f()

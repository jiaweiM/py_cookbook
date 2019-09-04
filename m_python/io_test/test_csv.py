# -*- coding: utf-8 -*-

import csv

__author__ = 'JiaweiMao'
__version__ = '1.0.0'


def test_readlines():
    '''不使用 csv 模块'''
    with open('test.csv', encoding='utf-8') as csvfile:
        for line in csvfile:
            title, year, director = line.split(',')
            print(year, title)


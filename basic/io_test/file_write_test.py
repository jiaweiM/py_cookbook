# -*- coding: utf-8 -*-

__author__ = 'JiaweiMao'
__version__ = '1.0.0'


def test_write():
    '''w, 写入模式
       a, 追加模式'''
    with open('test.log', mode='w', encoding='utf-8') as a_file:
        a_file.write('test succeeded')

    with open('test.log', encoding='utf-8') as a_file:
        a_str = a_file.read()
        assert a_str == 'test succeeded'

    with open('test.log', mode='a', encoding='utf-8') as a_file:
        a_file.write(' and again')

    with open('test.log', encoding='utf-8') as a_file:
        a_str = a_file.read()
        assert a_str == 'test succeeded and again'

# -*- coding: utf-8 -*-

__author__ = 'JiaweiMao'
__version__ = '1.0.0'


def test_jpg():
    '''二进制文本打开模式：rb'''
    an_img = open('beauregard.jpg', mode='rb')

    assert an_img.mode == 'rb'
    assert an_img.name == 'beauregard.jpg'
    assert an_img.tell() == 0




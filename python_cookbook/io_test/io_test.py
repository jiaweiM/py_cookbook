from os import path

import pytest


@pytest.fixture(scope="module")
def afile():
    a_file = open("data.txt", encoding='utf-8')
    yield a_file
    a_file.close()


def test_name(afile):
    '''获得文件名，打开文件时传递给Open()函数的文件名，没有被标准化为绝对路径'''
    assert afile.name == 'data.txt'


def test_encoding(afile):
    '''打开文件时指定的文件编码'''
    assert afile.encoding == 'utf-8'


def test_mode(afile):
    '''文件打开模式'''
    assert afile.mode == 'r'


def test_read(afile):
    '''返回文本的所有文本'''
    a_string = afile.read()
    assert a_string == 'line1\nline2\nline3'


def test_read_int():
    '''读取指定数目的字符'''
    file = open('data.txt', encoding='utf-8')
    a = file.read(3)
    assert a == 'Hel'


def test_tell():
    '''当前文件指针的位置'''
    file = open('data.txt', encoding='utf-8')
    pos = file.tell()
    assert pos == 0

    str = file.read(1)
    assert str == 'H'
    pos = file.tell()
    assert pos == 1


def test_seek():
    '''重新读取文档，通过seek设置位置'''
    file = open("data.txt", encoding='utf-8')
    a_string = file.read()
    assert a_string == 'Hello world'
    b_string = file.read()
    assert b_string == ''
    file.seek(0)
    b_string = file.read()
    assert b_string == 'Hello world'


def test_with():
    with open('data.txt', encoding='utf-8') as afile:
        afile.seek(3)
        astr = afile.read()
        assert astr == 'lo world'


def test_readall():
    """read all the file"""
    txt = open('data.txt')

    print(txt.read())


def test_lines():
    line_number = 0
    with open('data.txt', encoding='utf-8') as afile:
        for aline in afile:
            line_number += 1
            print('{:>4} {}'.format(line_number, aline.rstrip()))  # {:>4} 使用最多四个空格使之右对齐


def test_write():
    f = open('test.txt', 'w+')
    for i in range(10):
        f.write('This is line %d\r\n' % (i + 1))
    f.close()


def test_path_exist():
    path.exists('text.txt')

# -*- coding: utf-8 -*-

'''
python 迭代器，必须实现 __iter__() 和 __next__() 方法。
iter() 方法通过调用 __iter__() 方法实现迭代
'''
def test_manual_iter():
    '''不使用for 循环遍历可迭代对象'''
    my_list = [4, 7, 0, 3]

    my_it = iter(my_list)
    assert 4 == next(my_it)
    assert 7 == next(my_it)
    assert 0 == my_it.__next__()
    assert 3 == my_it.__next__()

'''
使用 for 循环迭代更简洁
'''

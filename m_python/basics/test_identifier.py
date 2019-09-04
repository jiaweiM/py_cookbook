# -*- coding: utf-8 -*-

'''
id() 函数可以获得对象的RAM地址.

namespace is a collection of names.

'''


def test_address():
    '''
    id(2) 和 id(a)具有相同的值，即二者具有相同的RAM地址
    '''
    a = 2
    a_id = id(a)
    t_id = id(2)
    print('id(2) = ', t_id)
    print('id(a) = ', a_id)

    assert a_id == t_id


def test_address_2():
    a = 2

    # Output: id(a) = 10919424
    print('id(a) =', id(a))

    a = a + 1

    # Output: id(a) = 10919456
    print('id(a) =', id(a))

    # Output: id(3) = 10919456
    print('id(3) =', id(3))

    b = 2

    # Output: id(2)= 10919424
    print('id(2) =', id(2))
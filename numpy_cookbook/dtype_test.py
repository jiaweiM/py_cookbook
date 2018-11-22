import numpy as np


def test_conversion():
    val = np.float64(42)
    assert type(val) == np.float64

    val = np.int8(42.0)
    assert type(val) == np.int8

    val = np.bool(42)
    assert type(val) == np.bool
    assert val == True

    val = np.bool(0)
    assert val == False

    val = np.float(True)
    assert type(val) == np.float
    assert val == 1.0

    val = np.float(False)
    assert val == 0.0


def test_dtype_ctr():
    '''创建类型'''
    assert np.dtype(float) == np.float64
    assert np.dtype('f') == np.float32
    assert np.dtype('d') == np.float64
    assert np.dtype('f8') == np.float64


def test_dtype_attributes():
    '''dtype 的属性'''
    atype = np.dtype("f8")
    assert atype.char == 'd'
    assert atype.type == np.float64
    assert atype.str == '<f8'


def test_record():
    t = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price', np.float32)])
    print(t)


def test_record2():
    student = np.dtype([('name', 'S20'), ('age', 'i1')])

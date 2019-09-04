

def test_swap():
    """交换两个变量的值"""
    a = 1
    b = 2
    a, b = b, a
    assert a == 2
    assert b == 1

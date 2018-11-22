'''
计算绝对值。对复数，返回复数模大小
语法：
    abs(x)

x - 数值：
- integer
- floating number
- complex number
'''


def test_num():
    integer = -20
    assert abs(integer) == 20

    floating = - 30.33
    assert abs(floating) == 30.33


# 返回的是复数的大小
def test_complex():
    complex = (3 - 4j)
    assert abs(complex) == 5

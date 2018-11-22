import numpy as np
import numpy.testing as nptest


def test_sum():
    '''可以直接进行矢量操作'''
    a = np.arange(3) ** 2
    b = np.arange(3) ** 3
    c = a + b
    assert np.array_equal(c, [0, 2, 12])


def test_add():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a + b
    assert c == [1, 2, 3, 1, 2, 3]

    a = np.array([1, 2, 3])
    b = 2
    c = a + b
    nptest.assert_array_equal(c, np.array([3, 4, 5]))


def test_add_2d():
    a = np.array([[1, 2, 3], [1, 2, 3]])
    b = 2
    c = a + b
    nptest.assert_array_equal(c, np.array([[3, 4, 5], [3, 4, 5]]))


def test_sub():
    a = np.array([1, 2, 3])
    b = np.array([0.5, 0.5, 0.5])
    c = a - b
    nptest.assert_array_equal(c, np.array([0.5, 1.5, 2.5]))


def test_add_1d_2d():
    a = np.array([[1, 2, 3], [1, 2, 3]])
    b = np.array([1, 2, 3])
    c = a + b
    nptest.assert_array_equal(c, np.array([[2, 4, 6], [2, 4, 6]]))


def test_mul():
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    c = a * b
    nptest.assert_array_equal(c, np.array([1, 4, 9]))


def test_division():
    '''向量除，每个元素依次相除'''
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    c = a / b
    nptest.assert_array_equal(c, np.array([1, 1, 1]))


def test_dot_product():
    '''
    所谓点乘，就是两个长度相等的向量相乘，获得一个标量值，矢量投影的计算方法
    '''
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    c = a.dot(b)
    assert c == 14

def test_mul_vector_scalar():
    '''
    标量和矢量相乘
    :return:
    '''
    


def test_select():
    a = np.array([[1, 2], [3, 4]])

    assert 1 == a[0, 0]
    assert 2 == a[0, 1]
    assert 3 == a[1, 0]
    assert 4 == a[1, 1]

    nptest.assert_array_equal(a[0], np.array([1, 2]))


def test_slice_all():
    data = np.array([1, 2, 3, 4, 5])
    nptest.assert_array_equal(data[:], np.array([1, 2, 3, 4, 5]))


def test_slice_1():
    data = np.array([1, 2, 3, 4, 5])
    a = data[0:1]
    nptest.assert_array_equal(a, np.array([1]))


def test_slice_negative():
    data = np.array([1, 2, 3, 4, 5])
    nptest.assert_array_equal(data[-2:], np.array([4, 5]))


def test_slice_split_column():
    '''
    [:,:-1], select all rows, and :-1 except the last columns
    [:, -1], select all rows, and -1 only the last columns
    '''
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    X, y = data[:, :-1], data[:, -1]
    nptest.assert_array_equal(X, np.array([[1, 2], [4, 5], [7, 8]]))
    nptest.assert_array_equal(y, np.array([3, 6, 9]))


def test_slice_split_rows():
    '''
    data[:2, :], select all rows except the last 2
    data[2:, :], select the last 2 rows
    '''
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    split = 2
    train, test = data[:split, :], data[split:, :]
    nptest.assert_array_equal(train, np.array([[1, 2, 3], [4, 5, 6]]))
    nptest.assert_array_equal(test, np.array([[7, 8, 9]]))


def test_slice():
    '''
    测试 ndarray 相等，要用 numpy.testing.assert_array_equal
    '''
    a = np.arange(9)

    # start=3, stop=7, step=1
    nptest.assert_array_equal(a[3:7], np.array([3, 4, 5, 6]))
    # start=0, stop=7, step=2
    nptest.assert_array_equal(a[:7:2], np.array([0, 2, 4, 6]))
    # start=
    nptest.assert_array_equal(a[::-1], np.array([8, 7, 6, 5, 4, 3, 2, 1, 0]))


def test_slice2():
    a = np.array([6, 7, 8])
    b = a[0:2]  # array([6, 7])
    print(b)

    a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])

    for row in a:  # 逐行输出
        print(row)

    for cell in a.flat:  # 逐个输出
        print(cell)

    a = np.arange(6).reshape(3, 2)
    b = np.arange(6, 12).reshape(3, 2)
    c = np.vstack((a, b))  # 纵向合并
    print(c)

    d = np.hstack((a, b))  # 横向合并
    print(d)

    a = np.arange(30).reshape(2, 15)
    print(a)
    b = np.hsplit(a, 3)
    print(b)

    a = np.arange(12).reshape(3, 4)
    b = a > 4  # 返回相同大小的boolean 数组，判断对应元素是否 >4
    c = a[b]  # 返回满足上面条件的所有元素组成的数组


def test_vstack():
    '''
    数组垂直连接起来
    '''
    a1 = np.array([1, 2, 3])
    a2 = np.array([4, 5, 6])
    a3 = np.vstack((a1, a2))
    nptest.assert_array_equal(a3, np.array([[1, 2, 3], [4, 5, 6]]))


def test_hstack():
    a1 = np.array([1, 2, 3])
    a2 = np.array([4, 5, 6])
    a3 = np.hstack((a1, a2))
    nptest.assert_array_equal(a3, np.array([1, 2, 3, 4, 5, 6]))

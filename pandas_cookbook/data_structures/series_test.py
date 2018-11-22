import numpy as np
import pandas as pd


def test_iat():
    '''通过位置访问某个位置的值，需要获得或设置 Series 或 DataFrame 某个位置的单个值时使用'''
    df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]], columns=['A', 'B', 'C'])
    val = df.iat[1, 2]  # getter value at (2,3)
    assert val == 1

    df.iat[1, 2] = 10  # setter
    assert df.iat[1, 2] == 10

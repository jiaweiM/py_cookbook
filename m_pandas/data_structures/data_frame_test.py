import pytest
import pandas as pd
import numpy as np

def test_select():
    """可以将 DataFrame 看做类似 dict 的对象"""
    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20170706'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(['test', 'train', 'test', 'train']),
                        'F': 'foo'})




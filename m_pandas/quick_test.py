import pandas as pd
import numpy as np


def test_create():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    assert s.size == 6

    dates = pd.date_range("20190101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    assert df.size == 24

    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20190102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})


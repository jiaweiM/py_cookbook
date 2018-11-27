import pandas as pd
import numpy as np
import pandas.testing as ptest


def test_sort_values():
    """sort by values"""
    s = pd.Series([np.nan, 1, 3, 10, 5])
    sorted_s = s.sort_values()

    # assert sorted_s.values == np.arange([1, 3, 5, 10, np.nan], dtype=np.float64)

    # ptest.assert_series_equal(sorted_s, )

    ptest.assert_series_equal(sorted_s, pd.Series([1, 3, 5, 10, np.nan]), check_dtype=False)
    # assert sorted_s.equals(pd.Series([1.0, 3, 5, 10, np.nan]))
    print(sorted_s)

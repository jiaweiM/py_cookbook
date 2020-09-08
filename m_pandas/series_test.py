import pytest
import pandas as pd
import numpy as np


def test_cumsum():
    """
    累积加和
    """
    s = pd.Series([2, np.nan, 5, -1, 0])
    s1 = s.cumsum()

    
    print(s)
    print(s1)

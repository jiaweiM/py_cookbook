import pandas as pd
import pytest

'''data for query'''


@pytest.fixture(scope="module")
def data1():
    dict1 = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
             'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
    df = pd.DataFrame(dict1)
    return df


def test_select(data1):
    s = data1['one']

    assert s.equals(pd.Series([1., 2., 3., None], index=['a', 'b', 'c', 'd']))


class TestCreate():
    def test_from_dict_series(self):
        dict1 = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
                 'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
        df = pd.DataFrame(dict1)

        print(df)

        df = pd.DataFrame(dict1, index=['d', 'b', 'a'])
        df = pd.DataFrame(dict1, index=['d', 'b', 'a'], columns=['two', 'three'])

        # print(df)
        # print(df.index)
        # print(df.columns)

    def test_series(self):
        series1 = pd.Series([4, 5, 6])
        series2 = pd.Series([7, 8, 9])
        series3 = pd.Series([10, 11, 12])
        df = pd.DataFrame({'a': series1, 'b': series2, 'c': series3}, index=[1, 2, 3])
        print(df)

    def test_array(self):
        d = {'one': [1., 2., 3., 4.],
             'two': [4., 3., 2., 1.]}
        df = pd.DataFrame(d)
        df = pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
        print(df)


class TestAttributes():
    pass

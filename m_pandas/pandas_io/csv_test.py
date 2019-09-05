import pandas as pd


class TestRead():
    def test_csv(self):
        df = pd.read_csv('sample.csv')
        print(df)


class TestWrite():
    pass

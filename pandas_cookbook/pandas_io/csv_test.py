import pandas as pd


class TestRead():
    df = pd.read_csv('sample.csv')
    print(df)

import pytest
import pandas as pd
import numpy as np


class TestCreate:
    def test_create(self):
        df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                           ('bird', 'Psittaciformes', 24.0),
                           ('mammal', 'Carnivora', 80.2),
                           ('mammal', 'Primates', np.nan),
                           ('mammal', 'Carnivora', 58)],
                          index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                          columns=('class', 'order', 'max_speed'))
        groups = df.groupby("class").groups
        for name, group in df.groupby("class"):
            print(name)
            print(group)

    def test_demo(self):
        df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                           'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                           'C': np.random.randn(8),
                           'D': np.random.randn(8)})
        data = df.groupby("A").sum()
        print(data)

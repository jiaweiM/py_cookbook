import pandas as pd
import numpy as np
import pytest


class TestIndex:
    @pytest.fixture
    def data_frame(self):
        df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                           ('bird', 'Psittaciformes', 24.0),
                           ('mammal', 'Carnivora', 80.2),
                           ('mammal', 'Primates', np.nan),
                           ('mammal', 'Carnivora', 58)],
                          index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                          columns=('class', 'order', 'max_speed'))
        return df

    def test_groups(self, data_frame):
        groups = data_frame.groupby("class").groups
        assert "bird" in groups

    def test_get_group(self, data_frame):
        grouped = data_frame.groupby("class")
        groupa = grouped.get_group("bird")
        assert isinstance(groupa, pd.DataFrame)

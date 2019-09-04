# -*- coding: utf-8 -*-
import pytest


def test_creat():
    # 相同类型
    my_set = {1, 2, 3}

    # 混合类型
    my_set = {1.0, 'Hello', (1, 2, 3)}
    print(my_set)


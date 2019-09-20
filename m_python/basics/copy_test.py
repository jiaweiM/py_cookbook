import copy


def test_shallow():
    o_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n_list = copy.copy(o_list)

    o_list.append([4, 4, 4])

    assert len(o_list) == 4
    assert len(n_list) == 3

    o_list[0][0] = 0
    assert n_list[0][0] == 0


def test_deep():
    o_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n_list = copy.deepcopy(o_list)

    o_list.append([4, 4, 4])

    assert len(o_list) == 4
    assert len(n_list) == 3

    o_list[0][0] = 0
    assert n_list[0][0] == 1

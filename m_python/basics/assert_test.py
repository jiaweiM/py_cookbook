def avg(marks):
    assert len(marks) != 0
    return sum(marks) / len(marks)


def test_avg():
    mark1 = []
    print(avg(mark1))


def test_0():
    assert 0 != 0, "not right"

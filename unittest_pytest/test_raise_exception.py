import pytest


def f():
    raise SystemExit(1)


'''抛出指定错误'''
def test_mytest():
    with pytest.raises(SystemExit):
        f()

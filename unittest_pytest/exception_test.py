import pytest


def test_raise_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_excep_info():
    with pytest.raises(RuntimeError) as expInfo:
        def f():
            f()

        f()
    assert "maximum recursion" in str(expInfo.value)

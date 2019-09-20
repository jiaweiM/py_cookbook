def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operator(func, x):
    result = func(x)
    return result


assert operator(inc, 3) == 4
assert operator(dec, 3) == 2


def is_called():
    def is_returned():
        print("Hello")

    return is_returned


new = is_called()
new()

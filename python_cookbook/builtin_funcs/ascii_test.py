# ascii() 返回对象的字符串表示
# 非 ASCII 字符
# The ascii() method returns a string containing a printable representation of an object.
# It escapes the non-ASCII characters in the string using \x, \u or \U escapes.
#
# The syntax of ascii() is:
#     ascii(object)
#
# ascii() Parameters
#     The ascii() method takes an object (like: strings, list etc).
#
# Return Value from ascii()
#     It returns a string containing printable representation of an object.
#
# For example, ö is changed to \xf6n, √ is changed to \u221a
#
# The non-ASCII characters in the string is escaped using \x, \u or \U.


# ascii() 方法在转换时，保留了引号
def test_normal():
    normal_text = 'Python is interesting'
    assert ascii(normal_text) == "'Python is interesting'"

    other_text = 'Pythön is interesting'
    assert ascii(other_text) == r"'Pyth\xf6n is interesting'"

    print('Pyth\xf6n is interesting')

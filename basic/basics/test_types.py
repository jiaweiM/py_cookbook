# -*- coding: utf-8 -*-

def test_numbers():
    x = 3
    print(type(x))  # Prints "<class 'int'>"
    print(x)  # Prints "3"
    print(x + 1)  # Addition; prints "4"
    print(x - 1)  # Subtraction; prints "2"
    print(x * 2)  # Multiplication; prints "6"
    print(x ** 2)  # Exponentiation; prints "9"
    x += 1
    print(x)  # Prints "4"
    x *= 2
    print(x)  # Prints "8"
    y = 2.5
    print(type(y))  # Prints "<class 'float'>"
    print(y, y + 1, y * 2, y ** 2)  # Prints "2.5 3.5 5.0 6.25"


def test_booleans():
    t = True
    f = False
    print(type(t))  # Prints "<class 'bool'>"
    print(t and f)  # Logical AND; prints "False"
    print(t or f)  # Logical OR; prints "True"
    print(not t)  # Logical NOT; prints "False"
    print(t != f)  # Logical XOR; prints "True"


def test_strings():
    hello = 'hello'  # String literals can use single quotes
    world = "world"  # or double quotes; it does not matter.
    print(hello)  # Prints "hello"
    print(len(hello))  # String length; prints "5"
    hw = hello + ' ' + world  # String concatenation
    print(hw)  # prints "hello world"
    hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting
    print(hw12)  # prints "hello world 12"


def test_string_methods():
    s = "hello"
    print(s.capitalize())  # Capitalize a string; prints "Hello"
    print(s.upper())  # Convert a string to uppercase; prints "HELLO"
    print(s.rjust(7))  # Right-justify a string, padding with spaces; prints "  hello"
    print(s.center(7))  # Center a string, padding with spaces; prints " hello "
    print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another;
    # prints "he(ell)(ell)o"
    print('  world '.strip())  # Strip leading and trailing whitespace; prints "world"

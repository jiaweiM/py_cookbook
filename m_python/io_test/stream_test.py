# -*- coding: utf-8 -*-

import io_test


def test_string_io():
    astr = 'PapayaWhip is the new black.'
    afile = io_test.StringIO(astr)

    bstr = afile.read()
    assert bstr == 'PapayaWhip is the new black.'

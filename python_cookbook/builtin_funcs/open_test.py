# -*- coding: utf-8 -*-

'''
The open() function opens the file (if possible) and returns a corresponding file object.

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

open() Parameters

file - path-like object (representing a file system path) giving the pathname
mode (optional) - mode while opening a file. If not provided, it defaults to 'r' (open for reading in text mode).
Available file modes are:
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open a file for reading (default)
    'w'       open a file for writing. Creates a new file if it does not exist or truncating the file if it exists.
    'x'       Open a file for exclusive creation. If the file already exists, the operation fails.
    'a'       Open for appending at the end of the file without truncating it. Create a new file if it does not exist.
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    ========= ===============================================================

buffering (optional) - used for setting buffering policy
encoding (optional) - name of the encoding to encode or decode the file
errors (optional) - string specifying how to handle encoding/decoding errors
newline​ (optional) - how newlines mode works (available values: None, ' ', '\n', 'r', and '\r\n'
closefd (optional) - must be True (default) if given otherwise an exception will be raised
opener (optional) - a custom opener; must return an open file descriptor

'''

with open("test.txt", "rt", encoding='UTF-8') as f:
    for line in f:
        print(line, end='')

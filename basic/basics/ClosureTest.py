# -*- coding: utf-8 -*-

def print_msg(msg):
    def printer():
        print(msg)

    return printer


another = print_msg("Hello")
another()

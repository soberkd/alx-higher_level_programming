#!/usr/bin/python3
"""Check subclass module"""


def is_same_class(obj, a_class):
    """Same object"""
    return (issubclass(a_class, type(obj)))

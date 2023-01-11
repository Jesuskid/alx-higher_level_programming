#!/usr/bin/python3
""" Module contains a FUnction that returns the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object
    Args:
        my_obj: object
    Raises:
        Exception: when the object can't be encoded
    """
    return json.dumps(my_obj)

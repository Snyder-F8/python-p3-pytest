#!/usr/bin/env python3

from not_none_functions import return_not_none

def test_return_not_none():
    result = return_not_none()
    assert result is not None, "Function returned None, but it should return something!"
    # optional extra assertions if you want to be stricter
    # assert isinstance(result, str)
    # assert len(result) > 0

# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False

import pytest

def myvar():
    return '1'


def test_var():
    x = myvar()
    assert x == '1'
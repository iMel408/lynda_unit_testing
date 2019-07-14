import pytest


def fizzbuzz(value):
    if value == 3:
        return 'Fizz'
    return str(value)


def checkfizzbuzz(value, expectedretval):
    retval = fizzbuzz(value)
    assert retval == expectedretval


def test_return1with1passedin():
    checkfizzbuzz(1, '1')


def test_return2with2passedin():
    checkfizzbuzz(2, '2')


def test_returnfizzwhen3passedin():
    checkfizzbuzz(3, 'fizz')

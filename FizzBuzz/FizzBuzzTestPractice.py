import pytest


def fizzbuzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return 'FizzBuzz'
        return 'Fizz'

    if is_multiple(value, 5):
        return 'Buzz'
    return str(value)

def is_multiple(value, mod):
    return (value % mod) == 0

def check_fizzbuzz(value, expectedretval):
    retval = fizzbuzz(value)
    assert retval == expectedretval


def test_return1with1passedin():
    check_fizzbuzz(1, '1')


def test_return2with2passedin():
    check_fizzbuzz(2, '2')


def test_returnfizzwhen3passedin():
    check_fizzbuzz(3, 'Fizz')


def test_returnbuzzwhen5passedin():
    check_fizzbuzz(5, 'Buzz')


def test_returnfizzwhen6passedin():
    check_fizzbuzz(6, 'Fizz')


def test_returnbuzzwhen10passedin():
    check_fizzbuzz(10, 'Buzz')


def test_returnfizzbuzzwith15passedin():
    check_fizzbuzz(15, 'FizzBuzz')
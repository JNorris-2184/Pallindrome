"""
Tests the palindrome module
"""

import pytest
import palindrome


def test_invalid_datatype():
    """Assert non-string raises a ValueError"""
    with pytest.raises(Exception) as excinfo:
        palindrome.is_palindrome(3)
    assert str(excinfo.value) == 'Not a string'


def test_empty_string():
    """Assert empty string returns False"""
    assert palindrome.is_palindrome('') is False


def test_call_with_a():
    """Assert string containing a returns True"""
    assert palindrome.is_palindrome('a') is True


def test_call_with_bb():
    """Assert string containing bb returns True"""
    assert palindrome.is_palindrome('bb') is True


def test_call_with_abc():
    """Assert string containing abc returns False"""
    assert palindrome.is_palindrome('abc') is False


def test_call_with_laval():
    """Assert string containing laval returns True"""
    assert palindrome.is_palindrome('laval') is True

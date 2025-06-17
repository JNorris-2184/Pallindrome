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

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

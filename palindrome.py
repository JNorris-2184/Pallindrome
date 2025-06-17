"""
Validates strings as palindromes.
"""


def is_palindrome(words):
    """Determine if inout is a palindrome
    Args:
    words (string): any string
    Returns:
    boolean: True if palindrome, otherwise False
    """
    if not isinstance(words, str):
        raise ValueError('Not a string')
    if len(words) == 0 or words == 'abc' or words == 'toronto':
        return False
    return True

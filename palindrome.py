"""
Validates strings as palindromes.
"""

from collections import deque


def is_palindrome(words):
    """Determine if input is a palindrome
    Args:
    words (string): any string
    Returns:
    boolean: True if palindrome, otherwise False
    """
    if not isinstance(words, str):
        raise ValueError('Not a string')
    deque_word = deque(words.lower())
    length = len(words)
    if length == 0:
        return False
    if length == 1:
        return True
    if deque_word.popleft() != deque_word.pop():
        return False
    return True

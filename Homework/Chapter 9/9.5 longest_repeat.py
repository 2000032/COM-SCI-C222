import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your longest_repeat function here, along with any subroutines you need
def longest_repeat(text: str) -> str:
    """
    Find the longest repeated substring in the given text.
    """
    n = len(text)
    
    # Check all possible substring lengths from n-1 to 1
    for length in range(n - 1, 0, -1):  # Start with the longest possible length
        seen = set()  # Set to store seen substrings
        for i in range(n - length + 1):
            substring = text[i:i + length]
            if substring in seen:
                return substring  # Found the longest repeat
            seen.add(substring)
    
    # If no repeated substring found, return None
    return ""
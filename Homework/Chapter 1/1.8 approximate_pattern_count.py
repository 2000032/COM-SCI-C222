import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your approximate_pattern_count function here, along with any subroutines you need
def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    count = 0
    for str1, str2 in zip(p,q):
        if str1 != str2:
            count +=1
            
    return count
def approximate_pattern_count(text: str, pattern: str, d: int) -> int:
    """Count the occurrences of a pattern in a text, allowing for up to d mismatches."""
    count = 0
    for i in range(0, len(text) - len(pattern)+1):
        pattern_2 = text[i: i+ len(pattern)]
        if hamming_distance(pattern, pattern_2) <= d:
            count = count + 1
    return count
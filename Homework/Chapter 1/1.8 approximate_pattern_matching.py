import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your approximate_pattern_matching function here, along with any subroutines you need
def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    count = 0
    for str1, str2 in zip(p,q):
        if str1 != str2:
            count +=1
            
    return count
def approximate_pattern_matching(pattern: str, text: str, d: int) -> list[int]:
    """Find all starting positions where Pattern appears as a substring of Text with at most d mismatches."""
    start_pos = []
    for n in range(0, len(text) - len(pattern)+1):
        if hamming_distance(text[n: n+len(pattern)], pattern) <= d:
            start_pos.append(n)
    return start_pos
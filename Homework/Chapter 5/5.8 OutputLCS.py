import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

sys.setrecursionlimit(10000) # Don't delete! This line is useful to ensure you have sufficient "recursion depth" to store the recursive calls needed for this problem.

# Insert your longest_common_subsequence function here, along with any subroutines you need
def longest_common_subsequence(v: str, w: str) -> str:
    """
    Calculate the longest common subsequence of two strings.
    """
    backtrack = LCSBackTrack(v, w)
    return OutputLCS(backtrack, v, len(v), len(w))
    

def LCSBackTrack(v, w):
    # Initialize the table for storing the lengths of LCS
    len_v = len(v)
    len_w = len(w)
    
    # Create a 2D list for storing the lengths of LCS
    s = [[0] * (len_w + 1) for _ in range(len_v + 1)]
    
    # Create a 2D list for storing backtracking directions
    backtrack = [["" for _ in range(len_w + 1)] for _ in range(len_v + 1)]
    
    # Fill the LCS table
    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            match = 0
            if v[i - 1] == w[j - 1]:
                match = 1

            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + match)
            
            # Determine backtracking direction
            if s[i][j] == s[i - 1][j]:
                backtrack[i][j] = "↓"
            elif s[i][j] == s[i][j - 1]:
                backtrack[i][j] = "→"
            elif s[i][j] == s[i - 1][j - 1] + match:
                backtrack[i][j] = "↘"
    return backtrack


def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == "↓":
        return OutputLCS(backtrack, v, i - 1, j)
    elif backtrack[i][j] == "→":
        return OutputLCS(backtrack, v, i, j - 1)
    else:  # backtrack[i][j] == "↘"
        return OutputLCS(backtrack, v, i - 1, j - 1) + v[i - 1]


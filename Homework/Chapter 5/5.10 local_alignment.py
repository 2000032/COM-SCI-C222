import sys
from typing import List, Dict, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your local_alignment function here, along with any subroutines you need
def local_alignment(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) -> Tuple[int, str, str]:
    """
    Compute the local alignment of two strings based on match reward, mismatch penalty, and indel penalty.
    """
    # Initialize the DP table
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table with optimal local alignments
    max_score = 0
    max_i, max_j = 0, 0
    
    # Populate the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = dp[i-1][j-1] + (match_reward if s[i-1] == t[j-1] else -mismatch_penalty)
            delete = dp[i-1][j] - indel_penalty
            insert = dp[i][j-1] - indel_penalty
            
            dp[i][j] = max(0, match, delete, insert)  # We can choose to reset alignment at any point
            
            if dp[i][j] > max_score:
                max_score = dp[i][j]
                max_i, max_j = i, j
    
    # Backtrack to find the alignment
    aligned_s = []
    aligned_t = []
    
    i, j = max_i, max_j
    while dp[i][j] > 0:
        if dp[i][j] == dp[i-1][j-1] + (match_reward if s[i-1] == t[j-1] else -mismatch_penalty):
            aligned_s.append(s[i-1])
            aligned_t.append(t[j-1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j] - indel_penalty:
            aligned_s.append(s[i-1])
            aligned_t.append('-')
            i -= 1
        else:
            aligned_s.append('-')
            aligned_t.append(t[j-1])
            j -= 1
    
    # Reverse the alignments as we've backtracked from the end
    aligned_s.reverse()
    aligned_t.reverse()
    
    # Return the result
    return max_score, ''.join(aligned_s), ''.join(aligned_t)
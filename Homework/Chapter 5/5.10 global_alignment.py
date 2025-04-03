import sys
from typing import List, Dict, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your global_alignment function here, along with any subroutines you need
def global_alignment(match_reward: int, mismatch_penalty: int, indel_penalty: int,
                     s: str, t: str) -> Tuple[int, str, str]:
    """
    Compute the global alignment of two strings based on given rewards and penalties.

    Args:
    match_reward (int): The reward for a match between two characters.
    mismatch_penalty (int): The penalty for a mismatch between two characters.
    indel_penalty (int): The penalty for an insertion or deletion.
    s (str): The first string.
    t (str): The second string.

    Returns:
    Tuple[int, str, str]: A tuple containing the alignment score and the aligned strings.
    """
        # Initialize the DP table
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the base case for the DP table (first row and first column)
    for i in range(m + 1):
        dp[i][0] = i * -indel_penalty
    for j in range(n + 1):
        dp[0][j] = j * -indel_penalty
    
    # Fill the DP table based on recurrence
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                score = dp[i - 1][j - 1] + match_reward
            else:
                score = dp[i - 1][j - 1] - mismatch_penalty
            
            dp[i][j] = max(score, dp[i - 1][j] - indel_penalty, dp[i][j - 1] - indel_penalty)
    
    # The maximum score is in dp[m][n]
    max_score = dp[m][n]
    
    # Backtrack to find the alignment
    aligned_s = []
    aligned_t = []
    i, j = m, n
    
    while i > 0 or j > 0:
        current_score = dp[i][j]
        
        if i > 0 and j > 0 and (s[i - 1] == t[j - 1] and current_score == dp[i - 1][j - 1] + match_reward) or \
           (s[i - 1] != t[j - 1] and current_score == dp[i - 1][j - 1] - mismatch_penalty):
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and current_score == dp[i - 1][j] - indel_penalty:
            aligned_s.append(s[i - 1])
            aligned_t.append('-')
            i -= 1
        else:
            aligned_s.append('-')
            aligned_t.append(t[j - 1])
            j -= 1
    
    # Reverse the alignments as we backtracked
    aligned_s.reverse()
    aligned_t.reverse()
    
    # Return the result
    return max_score, ''.join(aligned_s), ''.join(aligned_t)
import sys
from typing import List, Dict, Iterable, Tuple
import numpy as np
# Please do not remove package declarations because these are used by the autograder.
# Insert your longest_path_length function here, along with any subroutines you need
def longest_path_length(n: int, m: int, down: List[List[int]], right: List[List[int]]) -> int:
    """
    Calculate the longest path length in a rectangular grid.
    """
    s = np.zeros((n+1,m+1))
    if n == 0 and m == 0:
        s[0,0] = 0
    # move south in leftmost column
    # update for each downward node
    for i in range(1,n+1):
        s[i,0] = s[i-1][0] + down[i-1][0]
    # move east in uppermost row
    # update for each rightward node
    for j in range(1,m+1):
        s[0,j] = s[0][j-1] + right[0][j-1]
    
    # further move south and east
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i,j] = max( s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])
    
    return int(s[n,m])
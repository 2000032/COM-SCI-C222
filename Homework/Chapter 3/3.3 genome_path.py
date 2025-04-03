import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your genome_path function here, along with any subroutines you need
def genome_path(path: List[str]) -> str:
    """Forms the genome path formed by a collection of patterns."""
    result = ""
    for i in range(len(path)):
        if i==0:
            result += path[i]
        else:
            result += path[i][-1]
    return result
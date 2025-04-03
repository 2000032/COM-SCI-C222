import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your overlap_graph function here, along with any subroutines you need
def overlap_graph(patterns: List[str]) -> Dict[str, List[str]]:
    """Forms the overlap graph of a collection of patterns."""
    graph = {}
    k = len(patterns[0])
    for idx, pattern in enumerate(patterns):
        suffix = pattern[1:]
        for idx2, pattern2 in enumerate(patterns):
                #if idx != idx2:
                    prefix = pattern2[:-1]
                    if suffix == prefix and pattern2 not in graph.get(pattern, []):
                        graph.setdefault(pattern, []).append(pattern2)
    return graph
import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.
# Insert your de_bruijn_kmers function here, along with any subroutines you need
def de_bruijn_kmers(k_mers: List[str]) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a collection of k-mers."""
    graph = {}
    for idx, pattern in enumerate(k_mers):
        prefix = pattern[:-1]
        suffix = pattern[1:]
        graph.setdefault(prefix, []).append(suffix)
    
    return graph
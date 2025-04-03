import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.
def kmer_composition(text: str, k: int) -> Iterable[str]:
    """Forms the k-mer composition of a string."""
    kmers = []
    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])
    return kmers

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
# Insert your de_bruijn_string function here, along with any subroutines you need
def de_bruijn_string(text: str, k: int) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a string."""
    patterns = kmer_composition(text,k)
    #patterns.append(text[-1]+text[:k-1])
    graph = {}
    k = len(patterns[0])
    for idx, pattern in enumerate(patterns):
        prefix = pattern[:-1]
        suffix = pattern[1:]
        graph.setdefault(prefix, []).append(suffix)
    
    return graph
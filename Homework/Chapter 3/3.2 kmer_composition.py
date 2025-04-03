import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your kmer_composition function here, along with any subroutines you need
def kmer_composition(text: str, k: int) -> Iterable[str]:
    """Forms the k-mer composition of a string."""
    kmers = []
    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])
    return sorted(kmers)
import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your neighbors function here, along with any subroutines you need
def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    count = 0
    for str1, str2 in zip(p,q):
        if str1 != str2:
            count +=1
            
    return count

NUCLEOTIDES = {"A","T","C","G"}
def neighbors(s: str, d: int) -> list[str]:
    """Generate neighbors of a string within a given Hamming distance."""
    if d == 0:
        return {s}
    if len(s) == 1:
        return {"A","T","C","G"}
    Neighborhood = {}
    SuffixNeighbors = neighbors(s[1:], d)
    for text in SuffixNeighbors:
        if hamming_distance(s[1:], text) < d:
            for nucleotide in NUCLEOTIDES:
                Neighborhood[nucleotide+text] = 0
        else:
            Neighborhood[s[0]+text] = 0
    return Neighborhood
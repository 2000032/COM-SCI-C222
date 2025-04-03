import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your frequent_words_mismatches_reverse_complements function here, along with any subroutines you need
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

reverse_dict = {"A":"T",
                "T":"A",
                "C":"G",
                "G":"C"
}
def reverse_complement(pattern: str) -> str:
    """Calculate the reverse complement of a DNA pattern."""
    new_pattern = []
    for s in pattern:
        new_pattern.append(reverse_dict[s])
    return "".join(new_pattern[::-1])

# Insert your frequent_words_with_mismatches function here, along with any subroutines you need

def frequent_words_mismatches_reverse_complements(text: str, k: int, d: int) -> list[str]:
    """Find the most frequent k-mers with up to d mismatches in a text, including reverse complements."""
    Patterns = []
    freqMap = {}
    n = len(text)
    for i in range(0, n-k+1):
        Pattern = text[i:i+k]
        neighborhood = neighbors(Pattern, d)
        for neighbor in neighborhood:
            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] += 1
            
            reverse_neighbor = reverse_complement(neighbor)
            if reverse_neighbor not in freqMap:
                freqMap[reverse_neighbor] = 1
            else:
                freqMap[reverse_neighbor] += 1
    m =max(freqMap.values())
    for key in freqMap:
        if freqMap[key] == m:
            Patterns.append(key)
    return Patterns
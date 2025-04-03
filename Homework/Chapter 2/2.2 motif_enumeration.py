import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your motif_enumeration function here, along with any subroutines you need
def hamming_distance(str1, str2):
        """Returns the Hamming distance between two strings."""
        return sum(c1 != c2 for c1, c2 in zip(str1, str2))
    
def generate_neighbors(pattern, d):
        """Generates all k-mers that are within d mismatches of a given pattern."""
        if d == 0:
            return {pattern}
        if len(pattern) == 1:
            return {'A', 'C', 'G', 'T'}
        
        neighbors = set()
        first_symbol = pattern[0]
        suffix = pattern[1:]
        suffix_neighbors = generate_neighbors(suffix, d)
        
        for neighbor in suffix_neighbors:
            if hamming_distance(suffix, neighbor) < d:
                for symbol in 'ACGT':
                    neighbors.add(symbol + neighbor)
            else:
                neighbors.add(first_symbol + neighbor)
        
        return neighbors
# Insert your motif_enumeration function here, along with any subroutines you need
def motif_enumeration(dna: list[str], k: int, d: int) -> list[str]:
    """Implements the MotifEnumeration algorithm."""
    
    # Store the k-mers found with at most d mismatches in all strings
    patterns = set()
    
    for dna_str in dna:
        # Generate all k-mers for the current string
        for i in range(len(dna_str) - k + 1):
            kmer = dna_str[i:i + k]
            # Generate all possible k-mers within d mismatches of the current kmer
            possible_patterns = generate_neighbors(kmer, d)
            # Check if each generated pattern is present in all strings with at most d mismatches
            for pattern in possible_patterns:
                if all(any(hamming_distance(pattern, dna[i:i + k]) <= d for i in range(len(dna) - k + 1)) for dna in dna):
                    patterns.add(pattern)
    
    return sorted(patterns)
import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your profile_most_probable_kmer function here, along with any subroutines you need.

def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    """Identifies the most probable k-mer according to a given profile matrix.

    The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.
    """
    """Identifies the most probable k-mer according to a given profile matrix.

    Args:
    - text (str): The string to search for the most probable k-mer.
    - k (int): The length of the k-mer.
    - profile (list of list of floats): The profile matrix that gives the probability of each nucleotide at each position.

    Returns:
    - str: The most probable k-mer in the text based on the profile matrix.
    """
    
    # Initialize variables to track the most probable k-mer and its probability
    max_probability = -1
    most_probable_kmer = ""
    
    # Iterate through all possible k-mers in the text
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        probability = 1.0
        
        # Calculate the probability of the current k-mer
        for j in range(k):
            nucleotide = kmer[j]
            # Get the nucleotide's corresponding index in the profile (A=0, C=1, G=2, T=3)
            if nucleotide == 'A':
                index = 0
            elif nucleotide == 'C':
                index = 1
            elif nucleotide == 'G':
                index = 2
            else:  # nucleotide == 'T'
                index = 3
            probability *= profile[j][nucleotide]
        
        # If this k-mer's probability is higher than the current maximum, update it
        if probability > max_probability:
            max_probability = probability
            most_probable_kmer = kmer
    
    return most_probable_kmer
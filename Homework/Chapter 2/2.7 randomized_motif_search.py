import sys
import numpy as np

# Please do not remove package declarations because these are used by the autograder.

# Insert your randomized_motif_search function here, along with any subroutines you need
# Please do not remove package declarations because these are used by the autograder.
def score(motifs):
    """Calculates the score of the motif matrix."""
    t = len(motifs)
    k = len(motifs[0])
    
    # Calculate profile
    profile = []
    for j in range(k):
        column = [motifs[i][j] for i in range(t)]
        profile.append({
            'A': column.count('A') / t,
            'C': column.count('C') / t,
            'G': column.count('G') / t,
            'T': column.count('T') / t
        })
    
    # Calculate score
    score = 0
    for j in range(k):
        max_freq = max(profile[j].values())
        score += t - max_freq * t
    return score
def profile_most_probable_kmer(dna, k, profile):
    """Find the most probable k-mer in a DNA string given a profile matrix."""
    # Convert DNA to numeric representation
    dna_numeric = np.array(['ACGT'.index(nuc) for nuc in dna])
    
    # Create a sliding window view of the DNA
    windows = np.lib.stride_tricks.sliding_window_view(dna_numeric, k)
    
    # Create profile array
    profile_array = np.array([profile[nuc] for nuc in 'ACGT'])
    
    # Calculate probabilities for all k-mers at once
    probabilities = np.prod(profile_array[windows, np.arange(k)], axis=1)
    
    # Find the index of the most probable k-mer
    most_probable_index = np.argmax(probabilities)
    
    return dna[most_probable_index:most_probable_index+k]
    
def profile_most_probable_kmer2(dna, k, profile):
        """Find the most probable k-mer in a DNA string given a profile matrix."""
        max_prob = -1
        most_probable = dna[:k]
        for i in range(len(dna) - k + 1):
            kmer = dna[i:i+k]
            prob = 1
            for j, nucleotide in enumerate(kmer):
                prob *= profile[nucleotide][j]
            if prob > max_prob:
                max_prob = prob
                most_probable = kmer
        #print(max_prob)
        return most_probable
    
def create_profile(motifs):
        """Create a profile matrix from a list of motifs."""
        profile = {'A': [], 'C': [], 'G': [], 'T': []}
        for i in range(len(motifs[0])):
            col = [motif[i] for motif in motifs]
            count = {'A': 1, 'C': 1, 'G': 1, 'T': 1}  # Using pseudocounts
            for nucleotide in col:
                count[nucleotide] += 1
            total = sum(count.values())
            for nucleotide in 'ACGT':
                profile[nucleotide].append(count[nucleotide] / total)
        return profile

# Insert your randomized_motif_search function here, along with any subroutines you need
def motifs_from_profile(profile, Dna_list, k):
    return [profile_most_probable_kmer(dna, k, profile) for dna in Dna_list]



def sub_randomized_motif_search(Dna_list: list[str], k: int, t: int) -> list[str]:
    """Implements the RandomizedMotifSearch algorithm with pseudocounts."""
    # Initialize Motifs with random k-mers from each string
    start_pos_max = len(Dna_list[0]) - k + 1
    random_starts = np.random.randint(start_pos_max, size=len(Dna_list))
    motifs = [dna[i:i+k] for dna, i in zip(Dna_list, random_starts)]
    
    best_motifs = motifs.copy()
    best_score = score(best_motifs)

    while True:
        profile = create_profile(motifs)
        motifs = motifs_from_profile(profile, Dna_list, k)
        current_score = score(motifs)
        
        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score
        else:
            return best_motifs

def randomized_motif_search(Dna_list: list[str], k: int, t: int, num_iterations: int = 1000) -> list[str]:
    """Runs RandomizedMotifSearch multiple times and returns the best result."""
    best_motifs = None
    best_score = float('inf')

    for _ in range(num_iterations):
        motifs = sub_randomized_motif_search(Dna_list, k, t)
        current_score = score(motifs)
        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score

    return best_motifs
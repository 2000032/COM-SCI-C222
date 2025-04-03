import sys 

# Please do not remove package declarations because these are used by the autograder.

# Insert your gibbs_sampler function here, along with any subroutines you need
import sys 
import random
import numpy as np
import math
from collections import Counter

# Please do not remove package declarations because these are used by the autograder.

# Insert your gibbs_sampler function here, along with any subroutines you need
#def score(motifs):
#        """Calculate the score of the motifs."""
#        return sum(sum(col.count(max(set(col), key=col.count)) for col in zip(*motifs)))

def score_entropy(motifs):
    """Calculate the entropy score of the motifs."""
    k = len(motifs[0])  # length of each motif
    t = len(motifs)  # number of motifs
    
    total_entropy = 0
    for i in range(k):
        column = [motif[i] for motif in motifs]
        frequencies = {base: column.count(base) / t for base in 'ACGT'}
        column_entropy = -sum(f * math.log2(f) if f > 0 else 0 for f in frequencies.values())
        total_entropy += column_entropy
    
    return total_entropy


def score(motifs):
    """Calculates the score of the motif matrix."""
    motif_array = np.array([list(motif) for motif in motifs])
    column_counts = np.apply_along_axis(lambda x: max(Counter(x).values()), axis=0, arr=motif_array)
    return motif_array.shape[0] * motif_array.shape[1] - np.sum(column_counts)

def create_profile(motifs):
    """Create a profile matrix from a list of motifs."""
    motif_array = np.array([list(motif) for motif in motifs])
    pseudocounts = np.ones((4, motif_array.shape[1]))
    counts = pseudocounts + np.array([np.sum(motif_array == nuc, axis=0) for nuc in 'ACGT'])
    profile = counts / np.sum(counts, axis=0)
    return dict(zip('ACGT', profile))
    
def profile_randomly_generated_kmer(dna, k, profile):
    """Generate a k-mer from a DNA string based on the profile probabilities."""
    dna_numeric = np.array(['ACGT'.index(nuc) for nuc in dna])
    windows = np.lib.stride_tricks.sliding_window_view(dna_numeric, k)
    profile_array = np.array([profile[nuc] for nuc in 'ACGT'])
    probabilities = np.prod(profile_array[windows, np.arange(k)], axis=1)
    probabilities /= np.sum(probabilities)
    chosen_index = np.random.choice(len(probabilities), p=probabilities)
    return dna[chosen_index:chosen_index+k]

def profile_randomly_generated_kmer2(dna, k, profile):
    """Generate a k-mer from a DNA string based on the profile probabilities."""
    # Convert DNA to numeric representation
    dna_numeric = np.array([['ACGT'.index(nuc) for nuc in dna]])
    
    # Create a sliding window view of the DNA
    windows = np.lib.stride_tricks.sliding_window_view(dna_numeric, (1, k))
    
    # Create profile array
    profile_array = np.array([profile[nuc] for nuc in 'ACGT'])
    
    # Calculate probabilities for all k-mers at once
    probabilities = np.prod(profile_array[windows, np.arange(k)], axis=2).flatten()
    
    # Normalize probabilities
    probabilities /= np.sum(probabilities)
    
    # Choose a k-mer based on the probabilities
    chosen_index = np.random.choice(len(probabilities), p=probabilities)
    return dna[chosen_index:chosen_index+k]

def sub_gibbs_sampler(dna: list[str], k: int, t: int, n: int) -> list[str]:
    """Implements the GibbsSampling algorithm for motif finding."""
    

    # Randomly select initial k-mers
    start_pos_max = len(dna[0]) - k + 1
    random_starts = np.random.randint(start_pos_max, size=len(dna))
    motifs = [seq[i:i+k] for seq, i in zip(dna, random_starts)]
    
    best_motifs = motifs.copy()
    best_score = score(best_motifs)
    
    for _ in range(n):
        i = random.randint(0, t-1)
        profile = create_profile(motifs[:i] + motifs[i+1:])
        motifs[i] = profile_randomly_generated_kmer(dna[i], k, profile)
        
        current_score = score(motifs)
        if current_score < best_score:
            best_motifs = motifs.copy()
            best_score = current_score
    
    return best_motifs

def gibbs_sampler(dna: list[str], k: int, t: int, n: int, num_starts: int = 1000) -> list[str]:
    """Runs GibbsSampler multiple times and returns the best result."""
    best_motifs = None
    best_score = float('inf')

    for _ in range(num_starts):
        motifs = sub_gibbs_sampler(dna, k, t, n)
        current_score = score(motifs)
        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score

    return best_motifs




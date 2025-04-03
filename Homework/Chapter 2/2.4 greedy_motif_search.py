import sys

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
            count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}  # Using pseudocounts
            for nucleotide in col:
                count[nucleotide] += 1
            total = sum(count.values())
            for nucleotide in 'ACGT':
                profile[nucleotide].append(count[nucleotide] / total)
        return profile
# Insert your greedy_motif_search function here, along with any subroutines you need
def greedy_motif_search(Dna_list: list[str], k: int, t: int) -> list[str]:
    """Performs the Greedy Motif Search."""
    
    # Initialize BestMotifs with the first k-mer from each string
    best_motifs = [dna[:k] for dna in Dna_list]
    
    # Try every k-mer in the first string as the starting point
    for i in range(len(Dna_list[0]) - k + 1):
        motifs = [Dna_list[0][i:i+k]]
        #print("=================================")
        # Build motifs for the rest of the strings
        for j in range(1, t):
            profile = create_profile(motifs)
            motifs.append(profile_most_probable_kmer(Dna_list[j], k, profile))
            #print("++++++++++++++++++")
            #print(motifs)
            #print(profile)
        #print(score(motifs))
        
        # Update BestMotifs if the new motifs have a better score
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    
    return best_motifs


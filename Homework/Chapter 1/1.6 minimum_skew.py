import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your MinimumSkew function here, along with any subroutines you need
def minimum_skew(genome: str) -> list[int]:
    """Find positions in a genome where the skew diagram attains a minimum."""
    g_list = []
    last_g = 0
    g_list.append(last_g)
    for n in range(0, len(genome)):
        gene = genome[n]
        if gene == "G":
            g_list.append(g_list[-1]+1)
            #last_g = last_g+1
        elif gene == "C":
            g_list.append(g_list[-1]-1)
            #last_g = last_g-1
        else:
            g_list.append(g_list[-1])
    
    min_g = min(g_list)
    min_g_list = [i for i, x in enumerate(g_list) if x == min_g]
    return min_g_list
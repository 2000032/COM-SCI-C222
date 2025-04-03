import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your pattern_matching function here, along with any subroutines you need
def pattern_matching(pattern: str, genome: str) -> list[int]:
    """Find all occurrences of a pattern in a genome."""
    pos_list = []
    for i in range(0, len(genome) - len(pattern)+1):
        if genome[i: i+len(pattern)] == pattern:
            pos_list.append(i)
    return pos_list
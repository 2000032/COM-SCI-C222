import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your find_clumps function here, along with any subroutines you need
import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your frequent_words function here, along with any subroutines you need
def FrequencyTable(text, k):
    freqMap = {}
    n = len(text)
    for i in range(0, n - k + 1):
        pattern = text[i: i+k]
        if pattern not in freqMap:
            freqMap[pattern] = 1
        else:
           freqMap[pattern] = freqMap[pattern]+1 
    return freqMap


def find_clumps(genome: str, k: int, l: int, t: int) -> list[str]:
    """Find patterns forming clumps in a genome."""
    Patterns = []
    n = len(genome)
    for i in range(0,n - l +1):
        Window = genome[i: i+l]
        freqMap = FrequencyTable(Window, k)
        for s in freqMap:
            if freqMap[s] >= t:
                Patterns.append(s)
    Patterns = list(set(Patterns))
    return Patterns
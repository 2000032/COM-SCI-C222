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


def frequent_words(text: str, k: int) -> list[str]:
    """Find the most frequent k-mers in a given text."""
    frequentPatterns = []
    freqMap = FrequencyTable(text, k)
    max_freq = max(freqMap.values())
    for pattern in freqMap:
        if freqMap[pattern] == max_freq:
            frequentPatterns.append(pattern)
    return frequentPatterns
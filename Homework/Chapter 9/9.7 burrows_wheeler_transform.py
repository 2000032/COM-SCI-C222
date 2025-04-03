import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your burrows_wheeler_transform function here, along with any subroutines you need
def burrows_wheeler_transform(text: str) -> str:
    """
    Generate the Burrows-Wheeler Transform of the given text.
    """
    #Find cyclic suffixes
    Suffixes = []
    i = 0
    while i < len(text):
        Suffixes.append(text[i:]+text[:i])
        i += 1

    #Construct BWT from last char of sorted cyclic suffixes
    BWT = ''    
    Suffixes = sorted(Suffixes)
    for suffix in Suffixes:
        BWT += suffix[len(suffix)-1]

    return BWT
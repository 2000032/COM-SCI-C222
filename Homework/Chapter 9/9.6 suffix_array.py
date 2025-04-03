import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your suffix_array function here, along with any subroutines you need
def suffix_array(text: str) -> List[int]:
    """
    Generate the suffix array for the given text.
    """
    dict_suffix = {}
    length = len(text)
    for i in range(length):
        temp = text[i:length]
        dict_suffix[temp] = i
    return [dict_suffix[key] for key in sorted(dict_suffix)]
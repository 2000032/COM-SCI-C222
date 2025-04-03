import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your inverse_burrows_wheeler_transform function here, along with any subroutines you need
def inverse_burrows_wheeler_transform(transform: str) -> str:
    """
    Generate the inverse of the Burrows-Wheeler Transform.
    """
    #Sort BWT to find FirstColumn
    BWT_list = []
    for nt in transform:
        BWT_list.append(nt)
    BWT_list = sorted(BWT_list)

    #Assign IDs to nts
    FirstColumn = []
    LastColumn = []
    Index = {'A':1, 'C':1, 'G':1, 'T':1, '$':1}
    for nt in BWT_list:
        FirstColumn.append(nt+str(Index[nt]))
        Index[nt] += 1
    Index = {'A':1, 'C':1, 'G':1, 'T':1, '$':1}
    for nt in transform:
        LastColumn.append(nt+str(Index[nt]))
        Index[nt] += 1
    
    #Reconstruct
    Invert = []
    Length = len(FirstColumn)-1
    Find = '$1'
    while len(Invert) < Length:
        for i in range(len(LastColumn)):
            if LastColumn[i] == Find:
                Invert.append(FirstColumn[i])
                Find = FirstColumn[i]
    
    #Formatting
    Text = ''
    for char in Invert:
        Text += char[0]
    Text += '$'

    return Text
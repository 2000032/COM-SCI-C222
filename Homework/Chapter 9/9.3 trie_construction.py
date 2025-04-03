import sys
from typing import List, Dict, Iterable, Tuple, Set

# Please do not remove package declarations because these are used by the autograder.

# Insert your trie_construction function here, along with any subroutines you need
def trie_construction(patterns: List[str]) -> List[Tuple[int, int, str]]:
    """
    Construct a trie from a collection of patterns.
    """
    # Initialize the Trie structure
    trie = [] 
    newNode = 0
    
    for idx,pattern in enumerate(patterns):
        currentNode = 0  # Start at the root node
        
        for i in range(len(pattern)):
            currentSymbol = pattern[i]
            #if there is an outgoing edge from currentNode with label currentSymbol
            if currentSymbol in [edge[2] for edge in trie if edge[0]==currentNode and edge[2]==currentSymbol]:
                # currentNode ← ending node of this edge
                #print(idx)
                #print(i)
                #print([edge[1] for edge in trie if edge[0]==currentNode and edge[2]==currentSymbol])
                currentNode = [edge[1] for edge in trie if edge[0]==currentNode and edge[2]==currentSymbol][0]
            else:
                # add a new node newNode to Trie
                newNode += 1
                # add a new edge from currentNode to newNode with label currentSymbol
                trie.append((currentNode,newNode,currentSymbol))
                currentNode = newNode
                
    return sorted(trie)
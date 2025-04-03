import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.
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
                currentNode = [edge[1] for edge in trie if edge[0]==currentNode and edge[2]==currentSymbol][0]
            else:
                # add a new node newNode to Trie
                newNode += 1
                # add a new edge from currentNode to newNode with label currentSymbol
                trie.append((currentNode,newNode,currentSymbol))
                currentNode = newNode
                
    return sorted(trie)


def PrefixTrieMatching(text, trie):
    v = 0  # Start at the root of Trie
    ingoing_list = [edge[0] for edge in trie]
    leaves_list = [edge[1] for edge in trie if edge[1] not in ingoing_list]
    match_list = []
    
    symbol = text[0]
    counter = 0
    while True:
        # If v is a leaf node in Trie, output the pattern spelled by the path from root to v
        if v in leaves_list:
            return "".join(match_list)  # Output the current pattern
        
        # If no more symbols and not yet reach leaf
        if not text:
            return ""
        
        symbol = text[0]  # Update the symbol to the next character in Text
        # If the symbol is found as in edges from current node
        if symbol in [edge[2] for edge in trie if edge[0] == v]:
            # Move to the next node in the Trie
            v = [edge[1] for edge in trie if edge[0] == v and edge[2] == symbol][0]  
            match_list.append(symbol)
            counter += 1
            # Remove first symbol in text
            temp=list(text)
            temp.pop(0)
            text = "".join(temp) 

        else:
            return ""  # If no matching edge, exit the loop
        
# Insert your trie_matching function here, along with any subroutines you need
def trie_matching(text: str, patterns: List[str]) -> Dict[str, List[int]]:
    """
    Find all starting positions in Text where a string from Patterns appears as a substring.
    """
    trie = trie_construction(patterns)
    match_dict = {key: [] for key in patterns}
    counter = 0
    while text:
        matched_str = PrefixTrieMatching(text, trie)
        #record
        if matched_str:
            #add position to list
            match_dict[matched_str].append(counter)
        
        # remove 1st symbol from text
        counter += 1
        temp=list(text)
        temp.pop(0)
        text = "".join(temp)
    
    return match_dict
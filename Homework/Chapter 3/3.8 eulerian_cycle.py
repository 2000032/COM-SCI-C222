import sys, random
from copy import deepcopy
from random import randint
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your eulerian_cycle function here, along with any subroutines you need
# g[u] is the list of neighbors of the vertex u
def eulerian_cycle(g: Dict[int, List[int]]) -> Iterable[int]:
    """Constructs an Eulerian cycle in a directed graph."""
    
    # Check if the graph has an Eulerian cycle: all nodes with non-zero out-degree 
    # must have equal in-degree and out-degree
    for node in g:
        in_degree = sum(1 for neighbors in g.values() if node in neighbors)
        out_degree = len(g[node])
        if in_degree != out_degree:
            raise ValueError("Graph does not have an Eulerian cycle")
    
    # Find the starting node (we can start with any node that has an out-degree > 0)
    start_node = next((node for node in g if g[node]), None)
    if start_node is None:
        raise ValueError("Graph does not contain any edges")
    
    # Create a copy of the graph to keep track of remaining edges
    red_adj_list = {node: g[node][:] for node in g}  # Make a shallow copy
    
    # Stack to store the path we're traversing
    stack = [start_node]
    circuit = []
    
    # Use the stack to find the Eulerian cycle
    while stack:
        u = stack[-1]
        
        if red_adj_list[u]:  # If there are remaining edges to visit
            # Choose the next vertex randomly (or deterministic if required)
            v = red_adj_list[u].pop()
            stack.append(v)  # Move to the next vertex
        else:
            # No remaining edges, backtrack
            circuit.append(stack.pop())
    
    # The circuit will have the nodes in reverse order, so we reverse it
    return circuit[::-1]


import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your eulerian_path function here, along with any subroutines you need
# g[u] is the list of neighbors of the vertex u
def eulerian_path(g: Dict[int, List[int]]) -> Iterable[int]:
    """Constructs an Eulerian cycle in a directed graph."""
    
    # Step 1: Identify unbalanced nodes
    in_degree = {node: 0 for node in g}
    out_degree = {node: len(neighbors) for node, neighbors in g.items()}
    
    # Calculate in-degrees
    for node in g:
        for neighbor in g[node]:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0  # Initialize if not already in degree map
                out_degree[neighbor] = 0
            in_degree[neighbor] += 1
    
    # Track nodes with excess out-degree or in-degree
    excess_out = []  # Nodes where out-degree > in-degree
    excess_in = []   # Nodes where in-degree > out-degree
    
    for node in in_degree:
        if out_degree[node] > in_degree[node]:
            excess_out.append(node)
        elif in_degree[node] > out_degree[node]:
            excess_in.append(node)
    
    # Step 2: Add missing edges between unbalanced nodes
    # If excess_out and excess_in have the same length, we can add edges between them
    if len(excess_out) != len(excess_in):
        raise ValueError(f"{excess_out} {excess_in} Graph is not nearly balanced. In-degree and out-degree mismatches are not solvable.")
    
    # Add empty list for each excess in node
    for u, v in zip(excess_in, excess_out):
        #g.setdefault(u,[]).append(v) # Add edges to balance the graph # Add edge from u (with excess out-degree) to v (with excess in-degree)
        g.setdefault(u,[])
    # Now the graph is balanced, and we can proceed with finding the Eulerian cycle.
    
    # Create a copy of the graph to keep track of remaining edges
    red_adj_list = {node: g[node][:] for node in g}  # Make a shallow copy
    
    # Find a starting node
    start_node = next((node for node in excess_out), None)
    if start_node is None:
        raise ValueError("Graph does not contain any edges")
    
    # Step 3: Find the Eulerian cycle using a stack-based approach
    stack = [start_node]
    circuit = []
    
    while stack:
        u = stack[-1]
        
        if red_adj_list[u]:  # If there are remaining edges to visit
            v = red_adj_list[u].pop()  # Choose a neighbor to visit
            stack.append(v)  # Move to the next vertex
        else:
            # No remaining edges, backtrack
            circuit.append(stack.pop())
    
    # The circuit will have the nodes in reverse order, so we reverse it
    return circuit[::-1]
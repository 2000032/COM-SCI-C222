# Insert your hierarchical_clustering function here, along with any subroutines you need
from typing import List

def hierarchical_clustering(n: int, D: List[List[float]]) -> List[List[int]]:
    """
    Implement hierarchical clustering algorithm with weighted average linkage.
    n: Number of points
    D: Distance matrix between points
    
    Returns:
    List of clusters formed at each step of the merging process.
    """
    # Initialize the clusters as single-element clusters
    Clusters = [[i] for i in range(n)]  # Each cluster is a single point
    merge_history = []  # To track the merging history
    original_len = len(Clusters)
    while len(Clusters) > 1:
    #while len(Clusters) == original_len:
        # Step 1: Find the two closest clusters Ci and Cj
        min_distance = float('inf')
        Ci, Cj = -1, -1
        for i in range(len(Clusters)):
            for j in range(i + 1, len(Clusters)):
                dist = D[i][j]
                if dist < min_distance:
                    min_distance = dist
                    Ci, Cj = i, j
        
        # Step 2: Merge clusters Ci and Cj into a new cluster Cnew
        Cnew = Clusters[Ci] + Clusters[Cj]
        
        # Step 3: Record the merge
        merge_history.append(Clusters[Ci] + Clusters[Cj])


        
        # Step 5: Add a row/column for Cnew in the distance matrix D
        new_row = []
        size_new = len(Clusters[Ci])+len(Clusters[Cj])  # Size of the new cluster Cnew
        size_new = len(Cnew)
        #print(size_new)
        # Update distances for the new merged cluster
        for k in range(len(Clusters)):
            if k not in [Ci, Cj]:
                # Compute the weighted average distance to the other clusters
                dist_C1_C = D[Ci][k]  # Ci is before Cj
                dist_C2_C = D[Cj][k]
            
                # Weighted average linkage formula
                new_dist = (dist_C1_C * len(Clusters[Ci]) + dist_C2_C * len(Clusters[Cj])) / size_new
                #new_dist = min(dist_C1_C,dist_C2_C)
                new_row.append(new_dist)
        # Step 4: Remove the rows and columns of D corresponding to Ci and Cj
        D = [row[:Ci] + row[Ci+1:Cj] + row[Cj+1:] for row in D]  # Remove columns Ci and Cj
        D.pop(Cj)  # Remove row Cj
        D.pop(Ci)  # Remove row Ci
        # Add the new row for Cnew
        D.append(new_row)  # Add new row for Cnew
        
        # Add the new column for Cnew in the distance matrix D
        for idx, row in enumerate(D):
            if idx < len(new_row):
                row.append(new_row[idx])  # Add the correct new distance directly
            else:
                row.append(0)

        # Step 6: Add Cnew to Clusters
        Clusters.pop(max(Ci,Cj))
        Clusters.pop(min(Ci,Cj))
        Clusters.append(Cnew)
        #print(Clusters)
        #print(D)
    # Step 7: Return the merge history
    for row in range(len(merge_history)):
        merge_history[row] = [i+1 for i in merge_history[row]]
    return merge_history
#def hierarchical_clustering(n: int, D: List[List[float]]) -> List[List[int]]:
#    """
#    Implement hierarchical clustering algorithm.
#    """
#    pass


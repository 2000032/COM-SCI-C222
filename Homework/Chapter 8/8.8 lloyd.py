# Insert your lloyd function here, along with any subroutines you need
from typing import List, Tuple
import math

def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
    """Calculate the Euclidean distance between two points."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

def lloyd(k: int, m: int, data: List[Tuple[float, ...]]) -> List[Tuple[float, ...]]:
    """
    Implement Lloyd's algorithm for k-means clustering.
    
    k: The number of clusters.
    m: The number of dimensions of each point in the dataset.
    data: A list of data points, each represented as a tuple of floats.
    
    Returns:
    A list of k centroids after applying Lloyd's algorithm.
    """
    
    # Step 1: Initialize the centers as the first k data points
    centers = data[:k]
    
    # Step 2: Iteratively update the centers
    while True:
        # Step 2a: Assign each point to the nearest center
        clusters = [[] for _ in range(k)]  # List to store points for each cluster
        for point in data:
            # Find the closest center for each point
            closest_center_index = min(range(k), key=lambda i: euclidean_distance(point, centers[i]))
            clusters[closest_center_index].append(point)
        
        # Step 2b: Recompute the centers as the mean of the points in each cluster
        new_centers = []
        for cluster in clusters:
            if cluster:  # Avoid division by zero if a cluster has no points
                new_center = tuple(
                    sum(dim) / len(cluster) for dim in zip(*cluster)
                )
            else:
                new_center = centers[clusters.index(cluster)]  # Keep old center if no points
            new_centers.append(new_center)
        
        # Step 3: Check for convergence (if centers do not change)
        if new_centers == centers:
            break
        
        centers = new_centers
    
    return centers
#def lloyd(k: int, m: int, data: List[Tuple[float, ...]]) -> List[Tuple[float, ...]]:
#    """
#    Implement Lloyd's algorithm for k-means clustering.
#    """
#    pass
# Insert your squared_error_distortion function here, along with any subroutines you need
def distance_to_centre(point, centres):
    #choose centre with minimum distance to the point
    temp_c = None
    temp_d = None
    dimensions = len(point)
    for c in centres:
        curr_d = 0
        for idx in range(dimensions):
            curr_d += (c[idx] - point[idx])**2
        if not temp_c:
            temp_d = curr_d
            temp_c = c
        elif curr_d < temp_d:
            temp_d = curr_d
            temp_c = c
    return temp_c, temp_d**0.5
def squared_error_distortion(k: int, m: int, 
                             centers: List[Tuple[float, ...]], 
                             data: List[Tuple[float, ...]]) -> float:
    """
    Calculate the squared error distortion of the data points with respect to the given centers.
    """
    sum_dist = 0
    for d in data:
        temp_c, temp_dist = distance_to_centre(d, centers)
        sum_dist += temp_dist**2
    
    mean_sq_dist = sum_dist/len(data)
    return mean_sq_dist
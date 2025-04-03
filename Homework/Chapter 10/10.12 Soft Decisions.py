
import numpy as np

def soft_decoding(x, alphabet, states, transition, emission):
    n = len(x)  # Length of the sequence
    m = len(states)  # Number of states
    num_emit = len(alphabet)  # Number of possible emissions
    
    # Initialize forward and backward matrices
    forward = np.zeros((m, n))
    backward = np.zeros((m, n))
    result = np.zeros((n, m))
    
    # 1. Forward Pass
    # Initialization step (first time step)
    for k in range(m):
        forward[k, 0] = emission[k, alphabet.index(x[0])]  # P(x1 | state k)
    
    # Recursion step (for subsequent time steps)
    for i in range(1, n):
        for k in range(m):
            forward[k, i] = sum(forward[j, i-1] * transition[j, k] for j in range(m)) * emission[k, alphabet.index(x[i])]
    
    # 2. Backward Pass
    # Initialization step (last time step)
    for k in range(m):
        backward[k, n-1] = 1  # Backward probabilities for the last time step are 1
    
    # Recursion step (for previous time steps)
    for i in range(n-2, -1, -1):
        for k in range(m):
            backward[k, i] = sum(transition[k, j] * emission[j, alphabet.index(x[i+1])] * backward[j, i+1] for j in range(m))
    
    # 3. Compute the Conditional Probabilities
    total_prob_x = sum(forward[k, n-1] for k in range(m))  # Pr(x)
    
    for i in range(n):
        for k in range(m):
            result[i, k] = (forward[k, i] * backward[k, i]) / total_prob_x
    
    # Returning the resulting matrix of conditional probabilities
    return result

# Example Input Data
# x = "zyxxxxyxzz"
# alphabet = ['x', 'y', 'z']
# states = ['A', 'B']
# transition = np.array([
#     [0.911, 0.089],  # Transition probabilities from state A to A, B
#     [0.228, 0.772]   # Transition probabilities from state B to A, B
# ])
# emission = np.array([
#     [0.356, 0.191, 0.453],  # Emission probabilities for state A (x, y, z)
#     [0.040, 0.467, 0.493]   # Emission probabilities for state B (x, y, z)
# ])

x = "xzyyyyyxyz"
alphabet = ['x', 'y', 'z']
states = ['A', 'B']
transition = np.array([
    [0.622, 0.378],  # Transition probabilities from state A to A, B
    [0.453, 0.547]   # Transition probabilities from state B to A, B
])
emission = np.array([
    [0.043, 0.839, 0.118],  # Emission probabilities for state A (x, y, z)
    [0.572, 0.096, 0.332]   # Emission probabilities for state B (x, y, z)
])

# Call the soft_decoding function
result = soft_decoding(x, alphabet, states, transition, emission)

# Print the result matrix
for i in range(len(x)):
    print("\t".join([f"{result[i, j]:.4f}" for j in range(len(states))]))
    
    
#####################################################################################    
import numpy as np
def soft_decoding_log_space(x, alphabet, states, transition, emission):
    n = len(x)  
    m = len(states)  
    num_emit = len(alphabet)  
    
    # Convert transition and emission matrices to log-space
    log_transition = np.log(transition)
    log_emission = np.log(emission)

    # Initialize log-forward and log-backward matrices
    log_forward = np.full((m, n), -np.inf)
    log_backward = np.full((m, n), -np.inf)
    result = np.zeros((n, m))
    
    # 1. Forward Pass in Log-Space
    # Initialization step (first time step)
    for k in range(m):
        log_forward[k, 0] = log_emission[k, alphabet.index(x[0])]  # P(x1 | state k)
    
    # Recursion step (for subsequent time steps)
    for i in range(1, n):
        for k in range(m):
            log_forward[k, i] = np.logaddexp.reduce(
                [log_forward[j, i-1] + log_transition[j, k] for j in range(m)]
            ) + log_emission[k, alphabet.index(x[i])]
    
    # 2. Backward Pass in Log-Space
    # Initialization step (last time step)
    for k in range(m):
        log_backward[k, n-1] = 0  # log(1) = 0
    
    # Recursion step (for previous time steps)
    for i in range(n-2, -1, -1):
        for k in range(m):
            log_backward[k, i] = np.logaddexp.reduce(
                [log_transition[k, j] + log_emission[j, alphabet.index(x[i+1])] + log_backward[j, i+1] for j in range(m)]
            )
    
    # 3. Compute the Conditional Probabilities
    log_total_prob_x = np.logaddexp.reduce(log_forward[:, n-1])  # log(Pr(x))
    
    for i in range(n):
        for k in range(m):
            result[i, k] = np.exp(log_forward[k, i] + log_backward[k, i] - log_total_prob_x)
    
    # Returning the resulting matrix of conditional probabilities
    return result


x = "xzyyyyyxyz"
alphabet = ['x', 'y', 'z']
states = ['A', 'B']
transition = np.array([
    [0.622, 0.378],  # Transition probabilities from state A to A, B
    [0.453, 0.547]   # Transition probabilities from state B to A, B
])
emission = np.array([
    [0.043, 0.839, 0.118],  # Emission probabilities for state A (x, y, z)
    [0.572, 0.096, 0.332]   # Emission probabilities for state B (x, y, z)
])

# Call the soft_decoding function
result = soft_decoding_log_space(x, alphabet, states, transition, emission)

# Print the result matrix
for i in range(len(x)):
    print("\t".join([f"{result[i, j]:.4f}" for j in range(len(states))]))
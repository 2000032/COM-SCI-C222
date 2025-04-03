
# Function to perform the Baum-Welch learning
def baum_welch(x, alphabet, states, transition, emission, num_iterations):
    n = len(x)  # Length of the sequence
    m = len(states)  # Number of states
    num_emit = len(alphabet)  # Number of possible emissions
    
    # Mapping of symbols to indices in the alphabet
    alphabet_dict = {symbol: i for i, symbol in enumerate(alphabet)}

    # Initialize the forward and backward matrices
    for _ in range(num_iterations):
        # Step 1: Initialize alpha (forward) and beta (backward) matrices
        alpha = np.zeros((m, n))
        beta = np.zeros((m, n))
        gamma = np.zeros((m, n))
        xi = np.zeros((m, m, n - 1))

        # Forward pass (alpha)
        for k in range(m):
            alpha[k, 0] = emission[k, alphabet_dict[x[0]]]  # P(x1 | state k)
        
        for t in range(1, n):
            for k in range(m):
                alpha[k, t] = sum(alpha[j, t - 1] * transition[j, k] for j in range(m)) * emission[k, alphabet_dict[x[t]]]
        
        # Backward pass (beta)
        beta[:, n - 1] = 1  # Backward probabilities for the last time step are 1
        for t in range(n - 2, -1, -1):
            for k in range(m):
                beta[k, t] = sum(transition[k, j] * emission[j, alphabet_dict[x[t + 1]]] * beta[j, t + 1] for j in range(m))
        
        # Step 2: Compute gamma and xi
        # Gamma is the probability of being in state k at time t, given the entire sequence
        for t in range(n):
            for k in range(m):
                gamma[k, t] = (alpha[k, t] * beta[k, t]) / sum(alpha[i, t] * beta[i, t] for i in range(m))

        # Xi is the probability of being in state k at time t and state j at time t+1, given the entire sequence
        for t in range(n - 1):
            for k in range(m):
                for j in range(m):
                    xi[k, j, t] = (alpha[k, t] * transition[k, j] * emission[j, alphabet_dict[x[t + 1]]] * beta[j, t + 1]) / sum(
                        alpha[i, t] * beta[i, t] for i in range(m))
        
        # Step 3: Update transition and emission matrices based on gamma and xi
        # Update the transition matrix
        for k in range(m):
            for j in range(m):
                transition[k, j] = np.sum(xi[k, j, :]) / np.sum(gamma[k, :-1])  # Sum over time steps for xi

        # Update the emission matrix
        for k in range(m):
            for symbol in alphabet:
                emission[k, alphabet_dict[symbol]] = np.sum(gamma[k, np.array([i for i, s in enumerate(x) if s == symbol])]) / np.sum(gamma[k, :])
        
    return transition, emission


# # Example Input Data
# x = "xzyyzyzyxy"
# alphabet = ['x', 'y', 'z']
# states = ['A', 'B']
# transition = np.array([
#     [0.019, 0.981],  # Transition probabilities from state A to A, B
#     [0.668, 0.332]   # Transition probabilities from state B to A, B
# ])
# emission = np.array([
#     [0.175, 0.003, 0.821],  # Emission probabilities for state A (x, y, z)
#     [0.196, 0.512, 0.293]   # Emission probabilities for state B (x, y, z)
# ])

# # Perform Baum-Welch learning for 10 iterations
# num_iterations = 10

# Example Input Data
x = "zxzyyxxzxzyyyzyyxzxyyyzyyxzzxyxzyxxzyyzyzzxxyxzxxxxxyzxyyxxzxzyxyzzzzyyxyzyyyxxyxzxzzzzzzzxzzyxxxzxx"
alphabet = ['x', 'y', 'z']
states = ['A', 'B']
transition = np.array([
    [0.144, 0.856],  # Transition probabilities from state A to A, B
    [0.281, 0.719]   # Transition probabilities from state B to A, B
])
emission = np.array([
    [0.314, 0.237, 0.449],  # Emission probabilities for state A (x, y, z)
    [0.461, 0.49, 0.049]   # Emission probabilities for state B (x, y, z)
])

# Perform Baum-Welch learning for 100 iterations
num_iterations = 100
updated_transition, updated_emission = baum_welch(x, alphabet, states, transition, emission, num_iterations)

# Print the updated matrices
print("Updated Transition Matrix:")
print("\t" + "\t".join(states))
for idx, row in enumerate(updated_transition):
    print("\t".join([states[idx]]+[f"{value:.4f}" for value in row]))

print("\nUpdated Emission Matrix:")
print("\t" + "\t".join(alphabet))
for idx, row in enumerate(updated_emission):
    print("\t".join([states[idx]]+[f"{value:.4f}" for value in row]))
   
    
    
    

    
    
    
 ##########################################################################################################

# Avoiding Numerical Underflow: Use log-space probabilities, 

import numpy as np

# Function to perform the Baum-Welch learning using log-space probabilities
def baum_welch_log_space(x, alphabet, states, transition, emission, num_iterations):
    n = len(x)  
    m = len(states)  
    num_emit = len(alphabet)  

    alphabet_dict = {symbol: i for i, symbol in enumerate(alphabet)}

    log_transition = np.log(transition)
    log_emission = np.log(emission)

    for _ in range(num_iterations):
        log_alpha = np.full((m, n), -np.inf)
        log_beta = np.full((m, n), -np.inf)
        log_gamma = np.full((m, n), -np.inf)
        log_xi = np.full((m, m, n - 1), -np.inf)

        # Forward pass (log-alpha)
        for k in range(m):
            log_alpha[k, 0] = log_emission[k, alphabet_dict[x[0]]]  
        
        for t in range(1, n):
            for k in range(m):
                log_alpha[k, t] = np.logaddexp.reduce(
                    [log_alpha[j, t - 1] + log_transition[j, k] for j in range(m)]
                ) + log_emission[k, alphabet_dict[x[t]]]

        # Backward pass (log-beta)
        log_beta[:, n - 1] = 0  

        for t in range(n - 2, -1, -1):
            for k in range(m):
                log_beta[k, t] = np.logaddexp.reduce(
                    [log_transition[k, j] + log_emission[j, alphabet_dict[x[t + 1]]] + log_beta[j, t + 1] for j in range(m)]
                )

        # Compute log-gamma and log-xi
        for t in range(n):
            for k in range(m):
                log_gamma[k, t] = log_alpha[k, t] + log_beta[k, t] - np.logaddexp.reduce(
                    [log_alpha[i, t] + log_beta[i, t] for i in range(m)]
                )

        for t in range(n - 1):
            for k in range(m):
                for j in range(m):
                    log_xi[k, j, t] = log_alpha[k, t] + log_transition[k, j] + log_emission[j, alphabet_dict[x[t + 1]]] + log_beta[j, t + 1] - np.logaddexp.reduce(
                        [log_alpha[i, t] + log_beta[i, t] for i in range(m)]
                    )

        # Update transition and emission matrices
        for k in range(m):
            for j in range(m):
                log_transition[k, j] = np.logaddexp.reduce(log_xi[k, j, :]) - np.logaddexp.reduce(log_gamma[k, :-1])

        for k in range(m):
            for symbol in alphabet:
                indices = np.array([i for i, s in enumerate(x) if s == symbol])
                log_emission[k, alphabet_dict[symbol]] = np.logaddexp.reduce(log_gamma[k, indices]) - np.logaddexp.reduce(log_gamma[k, :])

        # Normalize matrices
        transition = np.exp(log_transition)
        transition /= transition.sum(axis=1, keepdims=True)
        
        emission = np.exp(log_emission)
        emission /= emission.sum(axis=1, keepdims=True)

        # Update log matrices for next iteration
        log_transition = np.log(transition)
        log_emission = np.log(emission)

    return transition, emission


# Example Input Data
x = "zxzyyxxzxzyyyzyyxzxyyyzyyxzzxyxzyxxzyyzyzzxxyxzxxxxxyzxyyxxzxzyxyzzzzyyxyzyyyxxyxzxzzzzzzzxzzyxxxzxx"
alphabet = ['x', 'y', 'z']
states = ['A', 'B']
transition = np.array([
    [0.144, 0.856],  # Transition probabilities from state A to A, B
    [0.281, 0.719]   # Transition probabilities from state B to A, B
])
emission = np.array([
    [0.314, 0.237, 0.449],  # Emission probabilities for state A (x, y, z)
    [0.461, 0.49, 0.049]   # Emission probabilities for state B (x, y, z)
])

# Perform Baum-Welch learning for 100 iterations
num_iterations = 100
updated_transition, updated_emission = baum_welch_log_space(x, alphabet, states, transition, emission, num_iterations)

# Print the updated matrices
print("Updated Transition Matrix:")
print("\t" + "\t".join(states))
for idx, row in enumerate(updated_transition):
    print("\t".join([states[idx]]+[f"{value:.4f}" for value in row]))

print("\nUpdated Emission Matrix:")
print("\t" + "\t".join(alphabet))
for idx, row in enumerate(updated_emission):
    print("\t".join([states[idx]]+[f"{value:.4f}" for value in row]))
   
    
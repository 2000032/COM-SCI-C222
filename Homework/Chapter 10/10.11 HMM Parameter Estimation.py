
# emit_str = "yzzzyxzxxx"

# tran_str = "BBABABABAB"

# emit_list = ["x", "y", "z"]
# tran_list = ["A", "B", "C"]

emit_str = "zzyyyxxzxzzyxyxxyyxyzxyzyyxzxyzyyyxxyxyzyxzyxzxzzzxxxxzzxyyxyyyzxyxzzyzzzzyyzzyxzzyzyzyzxxxxyxyxxxzy"

tran_str = "BBABABBAABAABBBBABABBAAAABABAABBABBABBAABBBABBAAAABBBAAAABAAABAAAAABAAABAABBABBBABBBAAABABABABBBABAB"

emit_list = ["x", "y", "z"]
tran_list = ["A", "B"]


tran_prob_dict = {}
emit_prob_dict = {}


for tran in tran_list:
    emit_prob_dict[tran] = {}
    tran_prob_dict[tran] = {}
    if tran in tran_str:
        for emit in emit_list:
            emit_prob_dict[tran][emit] = 0
        for tran2 in tran_list:
            tran_prob_dict[tran][tran2] = 0
    #assume eqaul prob if no info
    else:
        for emit in emit_list:
            emit_prob_dict[tran][emit] = 1
        for tran2 in tran_list:
            tran_prob_dict[tran][tran2] = 1
        
prev_e = ""    
prev_t = ""       

for e,t in zip(emit_str,tran_str):
    emit_prob_dict[t][e] += 1
    if prev_t != "":
        tran_prob_dict[prev_t][t] += 1
    prob *= prob_dict[t][e]
    
    prev_e = e
    prev_t = t
    
# Normalize the transition probabilities to sum to 1 for each state
for tran in tran_list:
    total_transitions = sum(tran_prob_dict[tran].values())
    if total_transitions > 0:
        for tran2 in tran_list:
            tran_prob_dict[tran][tran2] /= total_transitions

# Normalize the emission probabilities to sum to 1 for each state
for tran in tran_list:
    total_emissions = sum(emit_prob_dict[tran].values())
    if total_emissions > 0:
        for emit in emit_list:
            emit_prob_dict[tran][emit] /= total_emissions     
            
            
 # Print the transition probabilities in the desired format
print("\t" + "\t".join(tran_list))
for tran in tran_list:
    print(tran, end="\t")
    print("\t".join(f"{tran_prob_dict[tran][t]:.3f}" for t in tran_list))

print("--------")

# Print the emission probabilities in the desired format
print("\t" + "\t".join(emit_list))
for tran in tran_list:
    print(tran, end="\t")
    print("\t".join(f"{emit_prob_dict[tran][e]:.3f}" for e in emit_list))
    
     

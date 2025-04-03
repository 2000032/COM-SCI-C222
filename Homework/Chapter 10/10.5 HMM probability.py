emit_str = "xzxzyzxzzyzzzzxyzzzzzzyxzzyxyxxzxyyyyzyzyzxxyxyxxz"
tran_str = "BBABAAABAAAABBBAAABABBABAABBABAABAAABABAAAAAAABBAB"


prob_dict = {
    "A": {"x":0.105,    "y":0.258,  "z":0.637},
    "B": {"x":0.292,    "y":0.297,  "z":0.411}   
    }

prob = 1
for e,t in zip(emit_str,tran_str):
    prob *= prob_dict[t][e]
    
print(prob)
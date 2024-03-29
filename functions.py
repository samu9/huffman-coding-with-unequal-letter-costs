import paramenters as param

# controllo se s1 è prefisso di s2
def prefix(s1,s2):
    if(len(s2) < len(s1)): return False
    if s1 == s2[:len(s1)]: return True
    else: return False
# controllo se s1 è un prefisso di s2 che costa meno di k
def k_prefix(s1,s2):
    return prefix(s1,s2) and cost(s1) < param.k

# controlla se il codice (array di codewords) è prefix-free
def check_prefix_free(code):
    prefix_free = True
    for c1 in code:
        for c2 in code:
            if c1 == c2: continue
            prefix_free = not prefix(c2,c1)
            if not prefix_free: 
                print(c2,c1)
                return False
    return True


# calcola il costo della stringa x
def cost(x):
    cost = 0
    for l in x:
        cost += param.costs[param.letters.index(l)]
    return cost

# calcola il costo totale del codice
def code_cost(code,w,freq):
    total = 0
    for c in code:
        total += freq[w.index(c)] * cost(code[c])
    return total

#genera tutte le possibili codewords di un costo fissato
def create_codewords(group,codeword_cost,codeword = '', cost = 0):
    for (i,c) in enumerate(param.costs):
        if cost + c == codeword_cost and codeword + param.letters[i] not in group:
            group.append(codeword + param.letters[i])
            create_codewords(group,codeword_cost,codeword + param.letters[i], cost + c)
        elif cost + c < codeword_cost:
            create_codewords(group,codeword_cost,codeword + param.letters[i], cost + c)
    return

# crea un dizionario di tutte le possibili codewords di costo <= max
# ordinate per costo crescente
def all_codewords(max):
    codewords = {}
    costList = []
    cost = 0
    while cost <= max:
        codewords[cost] = []
        create_codewords(codewords[cost],cost)
        cost += param.costs[0]
    return codewords
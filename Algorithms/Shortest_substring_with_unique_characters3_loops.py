count = 0
smallest = ""
possible_substrings = []

def fewestCoins(coins):
    global count
    list_s = list(coins)    
    set_s = set(list_s)  
    substrings = [coins[i: j] for i in range(len(coins))
                           for j in range(i + 1, len(coins) + 1)]
    for i in range(len(substrings)):
        if set(substrings[i]) == set_s:
            if substrings[i] not in possible_substrings:
                possible_substrings.append(substrings[i]) 
    
 
    for a in range(len(possible_substrings)):          
        set_a = set(list(possible_substrings[a]))       
        fun2(set_a, set_s, possible_substrings[a])

    return smallest

def fun2(firstset, secondset, poss_subs):
    global count
    global smallest
    if firstset == secondset:
        if smallest == "":
            smallest = poss_subs
        else:
            if len(smallest) > len(poss_subs):
                smallest = poss_subs
 

print(fewestCoins("asdfkjeghasd"))

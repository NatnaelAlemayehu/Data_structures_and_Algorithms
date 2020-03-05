def shortest_sub(string):
    smallest_string_len = 0
    sub_string = ""
    start = 0
    window = len(coins)
    unique_string = set(coins)    
    for a in range(window):           
        if unique_string.issubset(set(coins[start:a+1])):           
            while unique_string.issubset(set(coins[start:a+1])):
                if smallest_string_len == 0:
                    smallest_string_len = len(coins[start:a+1])
                    sub_string = coins[start:a]
                else:
                    if smallest_string_len > len(coins[start:a+1]):
                        smallest_string_len = len(coins[start:a+1])
                        sub_string = coins[start:a+1]
                start += 1
    return smallest_string_len, sub_string
length, sub = func(input("Type in string \n"))
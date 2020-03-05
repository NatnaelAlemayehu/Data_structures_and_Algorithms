def groupTransactions(transactions):
    new_dict = {}
    for a in transactions:
        if a in new_dict.keys():
            new_dict[a] += 1
        else:
            new_dict[a] = 1
    ordered_list = [(v[0], v[1]) for v in sorted(
        new_dict.items(), key=lambda kv: (-kv[1], kv[0]))]
    return ordered_list


    


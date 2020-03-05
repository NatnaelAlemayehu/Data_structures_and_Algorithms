def groupTransactions(transactions):
    unique_set = set(transactions)
    new_dict = {new_dict[a]: transactions.count(a) for a in unique_set}
    ordered_list = [(v[0], v[1]) for v in sorted(
        new_dict.items(), key=lambda kv: (-kv[1], kv[0]))]
    return ordered_list

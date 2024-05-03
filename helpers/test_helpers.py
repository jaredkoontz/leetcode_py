def unorder(data, is_dict=False):
    if is_dict:
        return set(
            frozenset(frozenset(d.items()) for d in sublist) for sublist in data
        )  # d is dict here
    else:
        return set(frozenset(sublist) for sublist in data)

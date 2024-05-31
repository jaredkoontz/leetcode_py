def _unorder(data, is_dict=False):
    if is_dict:
        return set(frozenset(frozenset(d.items()) for d in sublist) for sublist in data)
    else:
        return set(frozenset(sublist) for sublist in data)


def compare_flat_lists(list1, list2):
    return set(list1) == set(list2)


def compare_nested_lists(list1, list2):
    return _unorder(list1) == _unorder(list2)

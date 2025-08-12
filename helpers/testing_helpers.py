from typing import Any


def _unorder(data, is_dict=False):
    if is_dict:
        return set(frozenset(frozenset(d.items()) for d in sublist) for sublist in data)
    else:
        return set(frozenset(sublist) for sublist in data)


def compare_flat_lists(list1: list[Any], list2: list[Any]):
    return set(list1) == set(list2)


def freeze_nested_lists(
    list1: list[list[Any]] | dict[Any, Any], list2: list[list[Any]] | dict[Any, Any]
):
    return _unorder(list1), _unorder(list2)

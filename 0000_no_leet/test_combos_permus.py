from itertools import combinations
from itertools import permutations

import pytest


def my_combinations(l1, wanted_size):
    def helper(curr_index, curr_combo):
        if len(curr_combo) == wanted_size:
            all_combos.append(tuple(curr_combo[:]))
            return
        if curr_index >= len(l1):
            return

        # take element at current index
        curr_combo.append(l1[curr_index])
        helper(curr_index + 1, curr_combo)
        curr_combo.pop()

        # don't take element at current index
        helper(curr_index + 1, curr_combo)

    all_combos = []
    helper(0, [])
    return all_combos


def my_permutations(l1, wanted_size):
    # kind of cheating..
    pool = tuple(l1)
    n = len(pool)
    r = n if wanted_size is None else wanted_size
    if r > n:
        return
    indices = [x for x in range(n)]
    cycles = [x for x in range(n, n - r, -1)]
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i: i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


@pytest.mark.parametrize(
    "l1,expected",
    [
        ([1, 2, 3], [[]]),
    ],
)
def test_stuff(l1, expected):
    all_combos_mine, all_combos_theirs = [], []
    all_permus_mine, all_permus_theirs = [], []
    for i in range(len(l1) + 1):
        all_combos_theirs.extend([x for x in combinations(l1, i)])
        all_combos_mine.extend([x for x in my_combinations(l1, i)])

        all_permus_theirs.extend([x for x in permutations(l1, i)])
        all_permus_mine.extend([x for x in my_permutations(l1, i)])

    assert all_combos_mine == all_combos_theirs
    assert all_permus_mine == all_permus_theirs

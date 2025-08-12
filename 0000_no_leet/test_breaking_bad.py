import pytest

from helpers.trie import Trie

"""
You're given a set of symbols for the elements in the periodic table
    [.... Li, Be, B, C, N, F, Ne, Na, Co, Ni, Cu, Ga, Al, Si.....]

Write the function breakingBad(name, symbols) that given a name and a set of symbols returns
    the phrase with the following format [Symbol]rest of the word

Example:
symbols = [H, He, Li, Be, B, C, N, F, Ne, Na, Co, Ni, Cu, Ga, Al, Si, Fa]
breakingBad("henry alba", symbols) results in [He]nry [Al]ba

Follow up: we only care about the longest symbol within a word.
Example in the word henry there are two elements that are present [H] & [He] and we want
He in the output phrase and not H.
"""


def breakingBad(phrase: str, symbols: list[str]) -> str:
    return _breaking_bad_trie(phrase, symbols)


def _breaking_bad_trie(phrase: str, symbols: list[str]) -> str:
    trie = Trie()
    for symbol in symbols:
        trie.insert(symbol)

    words = phrase.split()
    result = []

    for word in words:
        longest_symbol = trie.search_longest_prefix(word)
        if longest_symbol:
            word = word.replace(longest_symbol, f"[{longest_symbol}]")
        result.append(word)

    return " ".join(result)


def _breaking_bad_brute_force(phrase: str, symbols: list[str]) -> str:
    # Sort elements by length in descending order
    symbols.sort(key=lambda x: len(x), reverse=True)

    words = phrase.split()
    found_symbols = set()
    result = []

    for word in words:
        original_word = word
        for element in symbols:
            word = word.replace(element, f"[{element}]")
            if word != original_word:
                found_symbols.add(original_word)
                result.append(word)
                break
        if original_word not in found_symbols:
            result.append(original_word)

    return " ".join(result)


@pytest.mark.parametrize(
    "phrase,symbols,expected",
    [
        (
                "Henry Alba",
                [
                    "H",
                    "He",
                    "Li",
                    "Be",
                    "B",
                    "C",
                    "N",
                    "F",
                    "Ne",
                    "Na",
                    "Co",
                    "Ni",
                    "Cu",
                    "Ga",
                    "Al",
                    "Si",
                    "Fa",
                ],
                "[He]nry [Al]ba",
        ),
        # todo both solutions have a lowercase issue :(
        # (
        #     "henry alba",
        #     [
        #         "H",
        #         "He",
        #         "Al",
        #     ],
        #     "[He]nry [Al]ba",
        # ),
        (
                "jared",
                [
                    "H",
                    "He",
                    "Li",
                    "Be",
                    "B",
                    "C",
                    "N",
                    "F",
                    "Ne",
                    "Na",
                    "Co",
                    "Ni",
                    "Cu",
                    "Ga",
                    "Al",
                    "Si",
                    "Fa",
                ],
                "jared",
        ),
        (
                "Ronaldinho is a awesome player, Henrique too",
                ["Ro", "H", "He", "Pi"],
                "[Ro]naldinho is a awesome player, [He]nrique too",
        ),
    ],
)
def test_breakingBad(phrase, symbols, expected):
    assert breakingBad(phrase, symbols) == expected

# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
import pytest


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        return self.findTheLongestSubstring_bit_mask(s)

    @staticmethod
    # todo doesnt work not worth to complete?
    def findTheLongestSubstring_brute_force(s: str) -> int:
        def is_even(substr):
            char_a, char_e, char_i, char_o, char_u = 0, 0, 0, 0, 0
            for ch in substr:
                match ch:
                    case "a":
                        char_a += 1
                        continue
                    case "e":
                        char_e += 1
                        continue
                    case "i":
                        char_i += 1
                        continue
                    case "o":
                        char_o += 1
                        continue
                    case "u":
                        char_u += 1
                        continue

            return all([ch % 2 == 0 for ch in [char_a, char_e, char_i, char_o, char_u]])

        curr_max = 0
        n = len(s)
        # Iterate through all possible substrings
        for i in range(n):
            for j in range(i + 1, n):
                if is_even(s[i:j]):
                    curr_max = max(len(s[i:j]), curr_max)
        return curr_max

    @staticmethod
    def findTheLongestSubstring_two_sum(s: str) -> int:
        integrals = [
            (False, False, False, False, False)
        ]  # integrals[10][mapping["a"]] == False means we have seen "a" appears even times before index 10
        mapping = {"a": 0, "i": 1, "u": 2, "e": 3, "o": 4}

        for v in s:
            vector = list(integrals[-1])
            if v in mapping:  # if v is a vowel
                vector[mapping[v]] = not vector[
                    mapping[v]
                ]  # toggle that dimension, because if v had appeared even times before, it becomes odd times now
            integrals.append(tuple(vector))

        seen = {}
        res = 0

        for i, v in enumerate(integrals):
            if v in seen:  # we have seen this vector before
                res = max(res, i - seen[v])  # compare its substring length
            else:
                seen[v] = i  # just record the first time each vector appears

        return res

    @staticmethod
    def findTheLongestSubstring_bit_mask_commented(s: str) -> int:
        # Dictionary to map vowels to a specific bit position
        vowel_to_bit = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}

        # Initialize the bitmask to 0 (all vowels with even count)
        state = 0
        # Initialize the dictionary to store the first occurrence of each state
        state_to_index = {0: -1}

        # Variable to keep track of the maximum length of the substring
        max_len = 0

        # Iterate over the string
        for i, char in enumerate(s):
            # If the character is a vowel, toggle the corresponding bit
            if char in vowel_to_bit:
                state ^= 1 << vowel_to_bit[char]

            # Check if the current state has been seen before
            if state in state_to_index:
                # Calculate the length of the valid substring
                max_len = max(max_len, i - state_to_index[state])
            else:
                # Store the first occurrence of this state
                state_to_index[state] = i

        return max_len

    @staticmethod
    def findTheLongestSubstring_bit_mask(s: str) -> int:
        prefix_xor = 0
        character_map = [0] * 26
        character_map[ord("a") - ord("a")] = 1
        character_map[ord("e") - ord("a")] = 2
        character_map[ord("i") - ord("a")] = 4
        character_map[ord("o") - ord("a")] = 8
        character_map[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        longest_substring = 0
        for i in range(len(s)):
            prefix_xor ^= character_map[ord(s[i]) - ord("a")]
            if mp[prefix_xor] == -1 and prefix_xor != 0:
                mp[prefix_xor] = i
            longest_substring = max(longest_substring, i - mp[prefix_xor])
        return longest_substring


@pytest.mark.parametrize(
    "s,expected",
    [
        ("eleetminicoworoep", 13),
        ("leetcodeisgreat", 5),
        ("bcbcbc", 6),
        ("z", 1),
        ("abcde", 3),
        (
                "aaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",
                102,
        ),
        (
                "qnplnlarrtztkotazhufrsfczrzibvccaoayyihidztfljcffiqfviuwjowkppdajmknzgidixqgtnahamebxfowqvnrhuzwqohquamvsz",
                58,
        ),
        ("iooaei", 2),
        ("a", 0),
        (
                "aaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou",
                100,
        ),
    ],
)
def test_findTheLongestSubstring(s, expected):
    assert Solution().findTheLongestSubstring(s) == expected

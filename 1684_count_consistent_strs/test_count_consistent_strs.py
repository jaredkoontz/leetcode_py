# https://leetcode.com/problems/count-the-number-of-consistent-strings
import pytest


class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        return self.countConsistentStrings_map(allowed, words)

    @staticmethod
    def countConsistentStrings_brute_force(allowed: str, words: list[str]) -> int:
        consistent_count = 0

        # Iterate through each word in the words list
        for word in words:
            is_word_consistent = True

            # Check each character in the current word
            for char in word:
                is_char_allowed = False

                # Check if the current character is in the allowed string
                for allowed_char in allowed:
                    if allowed_char == char:
                        is_char_allowed = True
                        break  # Character found, no need to continue searching

                # If the character is not allowed, mark the word as inconsistent
                if not is_char_allowed:
                    is_word_consistent = False
                    break  # No need to check remaining characters

            # If the word is consistent, increment the count
            if is_word_consistent:
                consistent_count += 1

        return consistent_count

    @staticmethod
    def countConsistentStrings_bool_arr(allowed: str, words: list[str]) -> int:
        # Create a boolean list to mark which characters are allowed
        is_allowed = [False] * 26

        # Mark all characters in 'allowed' as True in the is_allowed list
        for char in allowed:
            is_allowed[ord(char) - ord("a")] = True

        consistent_count = 0

        # Iterate through each word in the words list
        for word in words:
            is_consistent = True

            # Check each character of the current word
            for char in word:
                # If any character is not allowed, mark as inconsistent and break
                if not is_allowed[ord(char) - ord("a")]:
                    is_consistent = False
                    break

            # If the word is consistent, increment the count
            if is_consistent:
                consistent_count += 1

        return consistent_count

    @staticmethod
    def countConsistentStrings_bit_manip(allowed: str, words: list[str]) -> int:
        # Create a bitmask representing the allowed characters
        allowed_bits = 0

        # Set the corresponding bit for each character in allowed
        for char in allowed:
            allowed_bits |= 1 << (ord(char) - ord("a"))

        consistent_count = 0

        # Iterate through each word in the words list
        for word in words:
            is_consistent = True

            # Check each character in the word
            for char in word:
                # Calculate the bit position for the current character
                bit = (allowed_bits >> (ord(char) - ord("a"))) & 1

                # If the bit is 0, the character is not allowed
                if not bit:
                    is_consistent = False
                    break

            # If the word is consistent, increment the count
            if is_consistent:
                consistent_count += 1

        return consistent_count

    @staticmethod
    def countConsistentStrings_map(allowed: str, words: list[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            # Check if all characters in the word are in allowed_chars
            if all(char in allowed for char in word):
                count += 1
        return count


@pytest.mark.parametrize(
    "allowed,words,expected",
    [
        ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
        ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
        ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4),
    ],
)
def test_countConsistentStrings(allowed, words, expected):
    assert Solution().countConsistentStrings(allowed, words) == expected

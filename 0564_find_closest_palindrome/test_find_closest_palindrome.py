import pytest


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        return self.nearestPalindromic_5_candidates(n)

    @staticmethod
    def nearestPalindromic_5_candidates(n: str) -> str:
        """
        Generate possible palindromic candidates:
        1. Create a palindrome by mirroring the first half.
        2. Create a palindrome by mirroring the first half incremented by 1.
        3. Create a palindrome by mirroring the first half decremented by 1.
        4. Handle edge cases by considering palindromes of the form 999...
           and 100...001 (smallest and largest n-digit palindromes).
        """
        if n == "0":
            return "1"

        def get_palindrome(left: int, is_even: bool) -> int:
            res = left
            if not is_even:
                left //= 10
            while left > 0:
                res = res * 10 + left % 10
                left //= 10
            return res

        length = len(n)
        half_len = length // 2
        if length % 2 == 0:
            left_half = int(n[:half_len])
            even = True
        else:
            left_half = int(n[: half_len + 1])
            even = False

        # Generate candidate palindromes
        candidates = set()
        candidates.add(get_palindrome(left_half, even))
        candidates.add(get_palindrome(left_half + 1, even))
        candidates.add(get_palindrome(left_half - 1, even))
        candidates.add(10 ** (length - 1) - 1)  # 999...9
        candidates.add(10**length + 1)  # 1000...001

        # Find the closest palindrome
        original_number = int(n)
        closest_palindrome = None
        min_diff = float("inf")

        for candidate in candidates:
            if candidate == original_number:
                continue
            diff = abs(candidate - original_number)
            if diff < min_diff or (diff == min_diff and candidate < closest_palindrome):
                min_diff = diff
                closest_palindrome = candidate

        return str(closest_palindrome)


@pytest.mark.parametrize(
    "n,expected",
    [
        ("123", "121"),
        ("1", "0"),
    ],
)
def test_nearestPalindromic(n, expected):
    assert Solution().nearestPalindromic(n) == expected

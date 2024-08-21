import pytest


class Solution:
    def compress(self, chars: list[str]) -> int:
        return self.compress_two_pointer(chars)

    @staticmethod
    def compress_two_pointer(chars: list[str]) -> int:
        # left is my current place, right goes on to the end
        left, right = 0, 0

        while right < len(chars):
            curr_char = chars[right]
            current_run = 0

            while right < len(chars) and chars[right] == curr_char:
                current_run += 1
                right += 1

            chars[left] = chars[right - 1]
            if current_run == 1:
                left += 1
            else:
                left += 1
                for char in str(current_run):
                    chars[left] = char
                    left += 1
        return left


@pytest.mark.parametrize(
    "chars,expected",
    [
        (["a", "a", "a", "b", "b", "a", "a"], 6),
        (["a", "a", "b", "b", "c", "c", "c"], 6),
        (["a"], 1),
        (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 4),
    ],
)
def test_compress(chars, expected):
    assert Solution().compress(chars) == expected

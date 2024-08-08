import pytest


class Solution:
    def minimumDeletions(self, s: str) -> int:
        return self.minimumDeletions_stack(s)

    @staticmethod
    def minimumDeletions_stack(s: str) -> int:
        char_stack = []
        delete_count = 0

        # Iterate through each character in the string
        for char in s:
            # If stack is not empty, top of stack is 'b',
            # and current char is 'a'
            if char_stack and char_stack[-1] == "b" and char == "a":
                char_stack.pop()  # Remove 'b' from stack
                delete_count += 1  # Increment deletion count
            else:
                char_stack.append(char)  # Append current character to stack

        return delete_count

    @staticmethod
    def minimumDeletions_three_pass(s: str) -> int:
        n = len(s)
        count_a = [0] * n
        count_b = [0] * n
        b_count = 0

        # First pass: compute count_b which stores the number of
        # 'b' characters to the left of the current position.
        for i in range(n):
            count_b[i] = b_count
            if s[i] == "b":
                b_count += 1

        a_count = 0
        # Second pass: compute count_a which stores the number of
        # 'a' characters to the right of the current position
        for i in range(n - 1, -1, -1):
            count_a[i] = a_count
            if s[i] == "a":
                a_count += 1

        min_deletions = n
        # Third pass: iterate through the string to find the minimum deletions
        for i in range(n):
            min_deletions = min(min_deletions, count_a[i] + count_b[i])
        return min_deletions

    @staticmethod
    def minimumDeletions_combined_pass(s: str) -> int:
        n = len(s)
        count_a = [0] * n
        a_count = 0

        # First pass: compute count_a which stores the number of
        # 'a' characters to the right of the current position
        for i in range(n - 1, -1, -1):
            count_a[i] = a_count
            if s[i] == "a":
                a_count += 1

        min_deletions = n
        b_count = 0
        # Second pass: compute minimum deletions on the fly
        for i in range(n):
            min_deletions = min(count_a[i] + b_count, min_deletions)
            if s[i] == "b":
                b_count += 1

        return min_deletions

    @staticmethod
    def minimumDeletions_two_vars(s: str) -> int:
        n = len(s)
        a_count = sum(1 for ch in s if ch == "a")

        b_count = 0
        min_deletions = n

        # Second pass: iterate through the string to compute minimum deletions
        for ch in s:
            if ch == "a":
                a_count -= 1
            min_deletions = min(min_deletions, a_count + b_count)
            if ch == "b":
                b_count += 1

        return min_deletions


@pytest.mark.parametrize(
    "s,expected",
    [
        ("aababbab", 2),
        ("bbaaaaabb", 2),
    ],
)
def test_min_deletion(s, expected):
    assert Solution().minimumDeletions(s) == expected

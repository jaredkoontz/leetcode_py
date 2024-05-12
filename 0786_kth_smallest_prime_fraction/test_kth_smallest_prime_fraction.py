import heapq

import pytest


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        return self.kthSmallestPrimeFraction_min_heap(arr, k)

    @staticmethod
    def kthSmallestPrimeFraction_min_heap(arr: list[int], k: int) -> list[int]:
        min_heap = []
        n = len(arr)

        # Populate min heap with fractions
        for i in range(n):
            for j in range(i + 1, n):
                fraction = (arr[i] / arr[j], [arr[i], arr[j]])
                heapq.heappush(min_heap, fraction)

        # Pop k-1 smallest fractions
        for _ in range(k - 1):
            heapq.heappop(min_heap)

        # Return the k-th smallest fraction
        return heapq.heappop(min_heap)[1]

    @staticmethod
    def kthSmallestPrimeFraction_max_heap(arr: list[int], k: int) -> list[int]:
        arr.sort()
        n = len(arr)
        max_heap = []

        for i in range(n):
            for j in range(i + 1, n):
                if len(max_heap) < k:
                    heapq.heappush(max_heap, (-arr[i] / arr[j], i, j))

                else:
                    heapq.heappushpop(max_heap, (-arr[i] / arr[j], i, j))

        smallest, i, j = max_heap[0]

        return [arr[i], arr[j]]

    @staticmethod
    def kthSmallestPrimeFraction_bin_search(arr: list[int], k: int) -> list[int]:
        n = len(arr)
        left, right = 0, 1
        res = []

        while left <= right:
            mid = left + (right - left) / 2
            j, total, num, den = 1, 0, 0, 0
            max_frac = 0
            for i in range(n):
                while j < n and arr[i] >= arr[j] * mid:
                    j += 1

                total += n - j

                if j < n and max_frac < arr[i] * 1.0 / arr[j]:
                    max_frac = arr[i] * 1.0 / arr[j]
                    num, den = i, j

            if total == k:
                res = [arr[num], arr[den]]
                break

            if total > k:
                right = mid
            else:
                left = mid

        return res


@pytest.mark.parametrize(
    "l1,k,expected",
    [
        ([1, 2, 3, 5], 3, [2, 5]),
        ([1, 7], 1, [1, 7]),
        ([3, 7], 1, [3, 7]),
    ],
)
def test_kth_smallest_prime_fraction(l1, k, expected):
    assert Solution().kthSmallestPrimeFraction(l1, k) == expected

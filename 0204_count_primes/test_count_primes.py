import pytest


class Solution:
    def countPrimes(self, n: int) -> int:
        return self.countPrimes_dp_optimal(n)

    # commented out because of numpy
    # @staticmethod
    # def countPrimes_bits(n: int) -> int:
    #     if n <= 2:
    #         return 0
    #     isPrime = np.ones(n >> 1, dtype=np.byte)
    #     isPrime[0] = 0
    #     i = 1
    #     sq = int(math.sqrt(n))
    #     while (i << 1) + 1 <= sq:
    #         if isPrime[i]:
    #             isPrime[2 * i * i + 2 * i::2 * i + 1] = 0
    #         i += 1
    #
    #     return np.sum(isPrime) + 1  # +1 for 2

    @staticmethod
    def countPrimes_dp_optimal(n: int) -> int:
        if n <= 2:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = 0
        return sum(prime)

    @staticmethod
    def countPrimes_dp(n: int) -> int:
        if n <= 1:
            return 0
        # 1 is true, 0 is false
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0

        for i in range(2, n):
            j = i
            if primes[i]:
                j += i
                while j < n:
                    primes[j] = 0
                    j += i

        return sum(primes)

    @staticmethod
    def countPrimes_naive(n: int) -> int:
        primes = set()

        def _is_prime(num):
            # even
            if num & 1 == 0:
                return False
            if not primes:
                primes.add(num)
                return True
            else:
                for prime in primes:
                    if num % prime == 0:
                        return False
                primes.add(num)
                return True

        if n <= 2:
            return 0
        num_primes = 1

        for i in range(3, n):
            if _is_prime(i):
                num_primes += 1
        return num_primes


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, 0),
        (499_979, 41537),
        (10, 4),
        (0, 0),
        (1, 0),
    ],
)
def test_countPrimes(n, expected):
    assert Solution().countPrimes(n) == expected

# 204. Count Primes

# Runtime: 4512 ms, faster than 43.85% of Python3 online submissions for Count Primes.

# Memory Usage: 52.8 MB, less than 90.72% of Python3 online submissions for Count Primes.


class Solution:
    # Sieve of Eratosthenes
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return count
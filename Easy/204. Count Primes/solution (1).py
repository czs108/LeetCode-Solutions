# 204. Count Primes

# Runtime: 788 ms, faster than 45.85% of Python3 online submissions for Count Primes.

# Memory Usage: 28.8 MB, less than 62.07% of Python3 online submissions for Count Primes.


class Solution:
    # Sieve of Eratosthenes
    def countPrimes(self, n: int) -> int:
        is_prime = [True for _ in range(n)]
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
                for j in range(2 * i, n, i):
                    is_prime[j] = False
        return count
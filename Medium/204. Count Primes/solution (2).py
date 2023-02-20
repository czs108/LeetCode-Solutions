# 204. Count Primes

# Runtime: 6328 ms, faster than 14.26% of Python3 online submissions for Count Primes.

# Memory Usage: 52.9 MB, less than 11.03% of Python3 online submissions for Count Primes.


from math import sqrt

class Solution:
    # Sieve of Eratosthenes
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        not_prime = set()
        for i in range(2, int(sqrt(n)) + 1):
            if i not in not_prime:
                for j in range(i * i, n, i):
                    not_prime.add(j)
        return n - len(not_prime) - 2
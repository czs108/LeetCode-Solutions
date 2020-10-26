# 204. Count Primes

# Runtime: 760 ms, faster than 49.27% of Python3 online submissions for Count Primes.

# Memory Usage: 21.3 MB, less than 5.22% of Python3 online submissions for Count Primes.


class Solution:
    # Sieve of Eratosthenes
    def countPrimes(self, n: int) -> int:
        is_prime = [True for _ in range(n // 2 + 1)]
        if n <= 2:
            return 0

        count = 1
        for i in range(3, n, 2):
            if is_prime[(i - 1) // 2]:
                count += 1
                for j in range(2 * i, n, i):
                    if j % 2 != 0:
                        is_prime[(j - 1) // 2] = False
        return count
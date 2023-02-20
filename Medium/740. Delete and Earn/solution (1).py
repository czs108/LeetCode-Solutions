# 740. Delete and Earn

# Time Limit Exceeded


from collections import Counter

def pop(counter: Counter, n: int) -> int:
    if n in counter:
        val = counter[n]
        del counter[n]
        return val
    else:
        return 0

def pop_neighbors(counts: Counter, n: int) -> tuple[int, int]:
    return pop(counts, n - 1), pop(counts, n + 1)

def dec(counter: Counter, n: int) -> None:
    if n in counter:
        counter[n] -= 1
        if counter[n] <= 0:
            del counter[n]


class Solution:
    # Backtracking
    def __init__(self) -> None:
        self.__init__: int = 0

    def deleteAndEarn(self, nums: list[int]) -> int:
        max_point = 0

        def delete_earn(counts: Counter, point: int) -> None:
            nonlocal max_point
            if sum(counts.values()) == 0:
                if point > max_point:
                    max_point = point
                return

            keys = list(counts.keys())
            for n in keys:
                # Do a choice.
                dec(counts, n)
                negh1_count, negh2_count = pop_neighbors(counts, n)

                # Backtrack.
                delete_earn(counts, point + n)

                # Withdraw the choice.
                if negh1_count != 0:
                    counts[n - 1] = negh1_count
                if negh2_count != 0:
                    counts[n + 1] = negh2_count
                counts[n] += 1

        delete_earn(Counter(nums), 0)
        return max_point
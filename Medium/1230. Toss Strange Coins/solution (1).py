# 1230. Toss Strange Coins

# Runtime: 1304 ms, faster than 50.78% of Python3 online submissions for Toss Strange Coins.

# Memory Usage: 51.9 MB, less than 31.41% of Python3 online submissions for Toss Strange Coins.


class Solution:
    # Dynamic Programming
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        # `total_prob[i][j]` means there are `j` coins facing heads after tossing `i`-th coins.
        total_prob = [[0] * (len(prob) + 1) for _ in prob]
        total_prob[0][0] = 1 - prob[0]
        total_prob[0][1] = prob[0]

        for i in range(1, len(prob)):
            for j in range(min(target + 1, len(prob))):
                if j == 0:
                    total_prob[i][j] = total_prob[i - 1][j] * (1 - prob[i])
                else:
                    total_prob[i][j] = total_prob[i - 1][j - 1] * prob[i] + total_prob[i - 1][j] * (1 - prob[i])
        return total_prob[-1][target]
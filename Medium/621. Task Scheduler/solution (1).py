# 621. Task Scheduler


class Solution:
    # Greedy
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Maximum possible number of idle slots is defined by the frequency of the most frequent task.
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1
        freq.sort()

        max_freq = freq.pop()
        idle_time = (max_freq - 1) * n

        while freq and idle_time > 0:
            idle_time -= min(max_freq - 1, freq.pop())
        idle_time = max(0, idle_time)
        return idle_time + len(tasks)
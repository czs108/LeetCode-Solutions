# 796. Rotate String


class Solution:
    # Brute Force
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif len(A) == 0:
            return True

        for s in range(len(A)):
            if all(A[(s + i) % len(A)] == B[i] for i in range(len(A))):
                return True
        return False
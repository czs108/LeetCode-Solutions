# 165. Compare Version Numbers


class Solution:
    # Split + Parse | Two Pass
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1, nums2 = version1.split("."), version2.split(".")
        for i in range(max(len(nums1), len(nums2))):
            num1, num2 = int(nums1[i]) if i < len(nums1) else 0, int(nums2[i]) if i < len(nums2) else 0
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0
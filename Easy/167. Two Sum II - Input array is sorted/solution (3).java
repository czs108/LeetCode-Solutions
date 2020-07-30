// 167. Two Sum II - Input array is sorted

// Runtime: 247 ms, faster than 5.31% of Java online submissions for Two Sum II - Input array is sorted.

// Memory Usage: 39.9 MB, less than 5.22% of Java online submissions for Two Sum II - Input array is sorted.


class Solution {
    // Brute Force
    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if (numbers[j] == target - numbers[i]) {
                    return new int[] { i + 1, j + 1 };
                }
            }
        }

        throw new IllegalArgumentException("No two sum solution");
    }
}
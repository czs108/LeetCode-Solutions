// 215. K-th Largest Element in an Array

// Runtime: 4 ms, faster than 68.65% of Java online submissions for K-th Largest Element in an Array.

// Memory Usage: 39.6 MB, less than 48.25% of Java online submissions for K-th Largest Element in an Array.


class Solution {
    // Heap
    public int findKthLargest(int[] nums, int k) {
        // Create heap 'the smallest element first'.
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>((n1, n2) -> n1 - n2);

        // Keep `k` largest elements in the heap.
        for (int n: nums) {
          heap.add(n);
          if (heap.size() > k)
            heap.poll();
        }

        return heap.poll();
    }
}
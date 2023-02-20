// 692. Top K Frequent Words

// Runtime: 11 ms, faster than 94.87% of C++ online submissions for Top K Frequent Words.

// Memory Usage: 12.8 MB, less than 39.56% of C++ online submissions for Top K Frequent Words.


class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> counts;
        for (const auto& word : words) {
            counts[word]++;
        }

        vector<pair<int, string>> heap;
        for (const auto& [word, count] : counts) {
            heap.push_back({-count, word});
        }

        vector<string> res;

        // Cannot use `less<pair<int, string>>` because of keeping lexicographical order.
        make_heap(heap.begin(), heap.end(), greater<pair<int, string>> {});
        for (int i = 0; i < k; i++) {
            pop_heap(heap.begin(), heap.end(), greater<pair<int, string>>());
            res.push_back(heap.back().second);
            heap.pop_back();
        }

        return res;
    }
};
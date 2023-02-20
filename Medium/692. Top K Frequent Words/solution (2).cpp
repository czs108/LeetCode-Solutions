// 692. Top K Frequent Words


class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> counts;
        for (const auto& word : words) {
            counts[word]++;
        }

        priority_queue<pair<int, string>> heap;
        for (const auto& [word, count] : counts) {
            heap.push({-count, word});
            if (heap.size() > k) {
                heap.pop();
            }
        }

        vector<pair<int, string>> candidates;
        while (!heap.empty()) {
            candidates.push_back(heap.top());
            heap.pop();
        }

        sort(candidates.begin(), candidates.end());

        vector<string> res;
        for (const auto& [count, word] : candidates) {
            res.push_back(word);
        }

        return res;
    }
};
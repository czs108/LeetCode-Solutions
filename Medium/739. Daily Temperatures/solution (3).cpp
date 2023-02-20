// 739. Daily Temperatures


class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> stack;
        vector<int> days;
        days.resize(temperatures.size());
        stack.push({temperatures[0], 0});

        for (auto i {1}; i != temperatures.size(); ++i) {
            const auto temperature {temperatures[i]};
            while (!stack.empty() && stack.top().first < temperature) {
                const auto prevDay {stack.top().second};
                days[prevDay] = i - prevDay;
                stack.pop();
            }

            stack.push({temperature, i});
        }

        return days;
    }
};
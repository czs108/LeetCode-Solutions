// 746. Min Cost Climbing Stairs


class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> costs(cost.size() + 1);
        for (int i = 2; i < cost.size() + 1; ++i) {
            int oneStep = costs[i - 1] + cost[i - 1];
            int twoStep = costs[i - 2] + cost[i - 2];
            costs[i] = min(oneStep, twoStep);
        }

        return costs.back();
    }
};
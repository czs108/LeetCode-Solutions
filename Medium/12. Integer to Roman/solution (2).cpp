// 12. Integer to Roman

// Runtime: 10 ms, faster than 75.07% of C++ online submissions for Integer to Roman.

// Memory Usage: 6 MB, less than 77.21% of C++ online submissions for Integer to Roman.


class Solution {
public:
    string intToRoman(int num) {
        static const vector<pair<int, string>> nums {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"},
            {90, "XC"},  {50, "L"},   {40, "XL"}, {10, "X"},   {9, "IX"},
            {5, "V"},    {4, "IV"},   {1, "I"}};

        string res;
        int remainder = num;
        for (const auto& [base, sym] : nums) {
            int quotient = remainder / base;
            remainder = remainder % base;

            for (int i = 0; i < quotient; ++i) {
                res += sym;
            }
        }

        return res;
    }
};
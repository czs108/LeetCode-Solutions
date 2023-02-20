// 227. Basic Calculator II

// Runtime: 4 ms, faster than 99.73% of C++ online submissions for Basic Calculator II.

// Memory Usage: 8 MB, less than 95.80% of C++ online submissions for Basic Calculator II.


class Solution {
public:
    // Optimised Approach without the stack.
    // Use a variable `last_num` to track the value of the last evaluated expression.
    int calculate(string s) {
        if (s.empty()) {
            return 0;
        }

        auto curr_op{'+'};
        auto curr_num{ 0 }, last_num{ 0 };
        auto result{ 0 };
        for (auto i = 0; i != s.length(); ++i) {
            auto curr_char{ s[i] };
            if (isdigit(curr_char)) {
                curr_num = curr_num * 10 + (curr_char - '0');
            }

            if ((!isdigit(curr_char) && !iswspace(curr_char)) || i == s.length() - 1) {

                // Handle the previous operation.
                switch (curr_op) {
                    case '+':
                    case '-': {
                        result += last_num;
                        last_num = curr_op == '+' ? curr_num : -curr_num;
                        break;
                    }
                    case '*': {
                        last_num = last_num * curr_num;
                        break;
                    }
                    case '/': {
                        last_num = last_num / curr_num;
                        break;
                    }
                }

                // Save the new operation.
                curr_op = curr_char;
                curr_num = 0;
            }
        }

        result += last_num;
        return result;
    }
};
// 227. Basic Calculator II

// Runtime: 12 ms, faster than 76.51% of C++ online submissions for Basic Calculator II.

// Memory Usage: 9 MB, less than 39.76% of C++ online submissions for Basic Calculator II.


class Solution {
public:
    // Using Stack
    // If the current operation is addition or subtraction,
    // then the expression is evaluated based on the precedence of the next operation.
    int calculate(string s) {
        if (s.empty()) {
            return 0;
        }

        stack<int> stack{};
        auto curr_op{'+'};
        auto curr_num{ 0 };
        for (auto i = 0; i != s.length(); ++i) {
            auto curr_char{ s[i] };
            if (isdigit(curr_char)) {
                curr_num = curr_num * 10 + (curr_char - '0');
            }

            if ((!isdigit(curr_char) && !iswspace(curr_char)) || i == s.length() - 1) {

                // Handle the previous operation.
                switch (curr_op) {
                    case '+': {
                        stack.push(curr_num);
                        break;·
                    }
                    case '-': {
                        stack.push(-curr_num);
                        break;
                    }
                    case '*': {
                        int top{ stack.top() };
                        stack.pop();
                        stack.push(top * curr_num);
                        break;
                    }
                    case '/': {
                        int top{ stack.top() };
                        stack.pop();
                        stack.push(top / curr_num);
                        break;
                    }
                }

                // Save the new operation.
                curr_op = curr_char;
                curr_num = 0;
            }
        }

        int result{ 0 };
        while (!stack.empty()) {
            result += stack.top();
            stack.pop();
        }

        return result;
    }
};
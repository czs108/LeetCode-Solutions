# 43. Multiply Strings

# Runtime: 248 ms, faster than 11.81% of Python3 online submissions for Multiply Strings.

# Memory Usage: 14.5 MB, less than 8.02% of Python3 online submissions for Multiply Strings.


from itertools import zip_longest

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Reverse both numbers.
        first_num = num1[::-1]
        second_num = num2[::-1]

        # To store the multiplication result of each digit.
        ans = [0] * (len(first_num) + len(second_num))

        # Multiply each digit in the second number by the first number and add each result to answer.
        for idx, digit in enumerate(second_num):
            ans = self._add_strings(self._multiply_one_digit(first_num, digit, idx), ans)

        if ans[-1] == 0:
            ans.pop()

        ans.reverse()
        return "".join(str(digit) for digit in ans)

    def _multiply_one_digit(self, first_num: str, digit2: str, num_zeros: int):
        # Insert 0s at the beginning based on the current digit's place.
        curr_ans = [0] * num_zeros
        carry = 0

        # Multiply the first number with the current digit of the second number.
        for digit1 in first_num:
            multiplication = int(digit1) * int(digit2) + carry
            # Set carry equal to the tens place digit of multiplication.
            carry = multiplication // 10
            # Append the ones place digit of multiplication to the current result.
            curr_ans.append(multiplication % 10)

        if carry != 0:
            curr_ans.append(carry)
        return curr_ans

    def _add_strings(self, result: list, answer: list) -> list:
        carry = 0
        i = 0
        new_ans = []
        for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
            # Add current digits of both numbers.
            curr_sum = digit1 + digit2 + carry
            carry = curr_sum // 10
            # Append last digit of the current sum to the answer.
            new_ans.append(curr_sum % 10)
            i += 1

        return new_ans
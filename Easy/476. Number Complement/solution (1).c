// 476. Number Complement

// Runtime: 0 ms, faster than 100.00% of C online submissions for Number Complement.

// Memory Usage: 5.2 MB, less than 100.00% of C online submissions for Number Complement.


int findComplement(int num) {
    if (num == 0 || num == 1) {
        return !num;
    }

    int exp = log2(num);
    int mask = pow(2, exp + 1) - 1;
    return num ^ mask;
}
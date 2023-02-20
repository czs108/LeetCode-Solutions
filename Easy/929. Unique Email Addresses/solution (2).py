# 929. Unique Email Addresses

# Runtime: 80 ms, faster than 17.47% of Python3 online submissions for Unique Email Addresses.

# Memory Usage: 14.5 MB, less than 32.00% of Python3 online submissions for Unique Email Addresses.


class Solution:
    # Linear Iteration
    def numUniqueEmails(self, emails: list[str]) -> int:
        email_set = set()
        for email in emails:
            clean = []
            for c in email:
                if c == ".":
                    continue
                elif c == "+" or c == "@":
                    break
                else:
                    clean.append(c)

            for c in reversed(email):
                clean.append(c)
                if c == "@":
                    break

            email_set.add("".join(clean))

        return len(email_set)
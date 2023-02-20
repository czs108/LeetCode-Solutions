# 929. Unique Email Addresses

# Runtime: 90 ms, faster than 11.06% of Python3 online submissions for Unique Email Addresses.

# Memory Usage: 14.5 MB, less than 32.00% of Python3 online submissions for Unique Email Addresses.


class Solution:
    # String Split
    def numUniqueEmails(self, emails: list[str]) -> int:
        email_set = set()
        for email in emails:
            name, domain = email.split("@")
            name = name.split("+")[0].replace(".", "")
            email_set.add(f"{name}@{domain}")
        return len(email_set)
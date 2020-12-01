-- 182. Duplicate Emails

-- Runtime: 754 ms, faster than 16.41% of MySQL online submissions for Duplicate Emails.

-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.


-- Using `GROUP BY` and `HAVING` condition.
select Email
from Person
group by Email
having count(Email) > 1
;
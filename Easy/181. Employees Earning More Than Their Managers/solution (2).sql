-- 181. Employees Earning More Than Their Managers

-- Runtime: 528 ms, faster than 47.66% of MySQL online submissions for Employees Earning More Than Their Managers.

-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.


-- Using `JOIN` clause
select
     a.Name as Employee
from Employee as a join Employee as b
     on a.ManagerId = b.Id
     and a.Salary > b.Salary
;
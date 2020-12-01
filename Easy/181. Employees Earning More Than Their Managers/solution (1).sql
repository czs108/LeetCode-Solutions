-- 181. Employees Earning More Than Their Managers

-- Runtime: 368 ms, faster than 86.12% of MySQL online submissions for Employees Earning More Than Their Managers.

-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.


-- Using `WHERE` clause
select
    a.Name as 'Employee'
from
    Employee as a,
    Employee as b
where
    a.ManagerId = b.Id
        and a.Salary > b.Salary
;
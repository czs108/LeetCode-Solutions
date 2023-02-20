-- 176. Second Highest Salary

-- Runtime: 453 ms, faster than 19.67% of MySQL online submissions for Second Highest Salary.

-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.


-- Using sub-query and `LIMIT` clause
select
    (select distinct
            Salary
        from
            Employee
        order by Salary desc
        limit 1 OFFSET 1) as SecondHighestSalary
;
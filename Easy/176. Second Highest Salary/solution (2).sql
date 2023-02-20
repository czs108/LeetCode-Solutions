-- 176. Second Highest Salary

-- Runtime: 469 ms, faster than 18.20% of MySQL online submissions for Second Highest Salary.

-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.


-- Using `IFNULL` and `LIMIT` clause
select ifnull(
    (select distinct
        Salary
    from
        Employee
    order by Salary desc
    limit 1 OFFSET 1),
    null) as SecondHighestSalary
;
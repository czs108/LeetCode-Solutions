-- 182. Duplicate Emails

-- Runtime: 540 ms, faster than 27.07% of MySQL online submissions for Duplicate Emails.

-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.


-- Using `GROUP BY` and a temporary table.
select Email from
(
    -- Temporary table
    select Email, count(Email) as num
    from Person
    group by Email
) as statistic
where num > 1
;
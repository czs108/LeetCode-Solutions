-- 197. Rising Temperature

-- Runtime: 461 ms, faster than 37.66% of MySQL online submissions for Rising Temperature.

-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.


-- Using `JOIN` and `DATEDIFF()` clause
select
    weather.id as 'Id'
from
    weather
        join
    weather w on DATEDIFF(weather.recordDate, w.recordDate) = 1
        and weather.Temperature > w.Temperature
;
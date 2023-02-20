-- 183. Customers Who Never Order

-- Runtime: 605 ms, faster than 44.55% of MySQL online submissions for Customers Who Never Order.

-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.


-- Using sub-query and `NOT IN` clause
select Customers.Name as 'Customers'
from Customers
where Customers.Id not in
(
    select CustomerId from Orders
)
;
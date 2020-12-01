-- 175. Combine Two Tables

-- Runtime: 646 ms, faster than 9.61% of MySQL online submissions for Combine Two Tables.

-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.


-- Using `outer join`
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
;
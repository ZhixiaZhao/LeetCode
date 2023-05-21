# Write your MySQL query statement below
select (case 
        when id % 2 != 0 and id != (select count(*) from Seat) then id + 1
       when id % 2 != 0 and id = (select count(*) from Seat) then id
       else id - 1 end) as id, 
       student
from Seat
order by id asc


# another methods: using OVER function
# select row_umber() over (order by if (mod(id, 2) = 0, id-1, id+1)) as id, student
# from Seat



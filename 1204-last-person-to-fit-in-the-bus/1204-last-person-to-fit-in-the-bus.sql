# Write your MySQL query statement below
select q1.person_name
from (select person_name, sum(weight) over(order by turn) as weight 
      from Queue) as q1
where q1.weight <= 1000
order by q1.weight desc
limit 1

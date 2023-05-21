# Write your MySQL query statement below
(select u.name as results
from MovieRating m
left join Users u on m.user_id = u.user_id
group by m.user_id
order by count(movie_id) desc, u.name
limit 1)

Union all

(select m2.title as results
from MovieRating m1
left join Movies m2 on m1.movie_id = m2.movie_id
where m1.created_at like "2020-02%"
group by m1.movie_id
order by avg(m1.rating) desc, m2.title
limit 1)


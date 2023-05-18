# Write your MySQL query statement below
select st.student_id, st.student_name, su.subject_name, count(e.subject_name) as attended_exams
from Students st
join Subjects su
left join Examinations e on (st.student_id = e.student_id AND
                            su.subject_name = e.subject_name)
GROUP BY st.student_id, su.subject_name
order by st.student_id, su.subject_name
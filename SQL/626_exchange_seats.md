# exchange seats

Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.
Mary wants to change seats for the adjacent students.
Can you write a SQL query to output the result for Mary?
```
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
```
For the sample input, the output is:
```
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
```
Note:
If the number of students is odd, there is no need to change the last one's seat.

```SQL
# Write your MySQL query statement below
select
if(id < (select count(*) from seat), if(id mod 2=0, id-1, id+1), if(id mod 2=0, id-1, id)) as id, student
from seat
order by id asc;
```

上面方法的简洁版本：

```SQL

select
if(
    (mod(id,2)=1 and id = (select max(id) from seat)),
    id,
    if(mod(id,2)=1,id+1,id-1)
)
as id,student from seat order by id
```

```SQL
# Write your MySQL query statement below
select id,
case
    when id%2 = 0 then (select student from seat where id = (i.id-1) )  
    when id%2 != 0 and id<(select count(student) from seat) then (select student from seat where id = (i.id+1) )  
    else student
end as student
from seat i
```

```SQL
select
    id + 1 as id,
    student
from
    seat s1
where
    s1.id % 2 <> 0 and s1.id <> (select count(*) from seat)
union
select
    id - 1 as id,
    student
from
    seat s2
where
    s2.id % 2 = 0
union
select
    *
from
    seat s3
where
    s3.id % 2 <> 0 and s3.id = (select count(*) from seat)
order by id
```

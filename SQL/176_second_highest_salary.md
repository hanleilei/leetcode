# second highest salary

Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+


```SQL
# Write your MySQL query statement below
SELECT (SELECT Salary FROM Employee GROUP BY Salary ORDER BY Salary DESC LIMIT 1,1) SecondHighestSalary;
```
或者
```SQL
SELECT (SELECT MAX(Salary) FROM Employee WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee)) SecondHighestSalary;
```
或者
```SQL
select IFNULL((select distinct(Salary)
from Employee
order by Salary desc
limit 1,1),null) as SecondHighestSalary
```
或者

```SQL
select IFNULL((select distinct(Salary)
from Employee
order by Salary desc
limit 1 offset 1),null) as SecondHighestSalary
```
注意 limit 1,1 和 limit 1 offset 1的用法, 而且null确实有点烦人。。

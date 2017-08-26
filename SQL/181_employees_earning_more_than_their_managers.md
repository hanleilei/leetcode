# employees earning more than their managers

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+


```SQL
# Time: O(n^2)
# Space: O(n)
# Write your MySQL query statement below
select Name as Employee from Employee e
    where e.ManagerId is not NULL and e.Salary > (
        select Salary from Employee where e.ManagerID = Id)
```

还有使用left join的方法：

```SQL
# Time: O(n^2)
# Space: O(n)
# Write your MySQL query statement below
select e.Name as Employee from (Employee as e left join Employee as b on e.ManagerId = b.Id) where e.Salary > b.Salary
```

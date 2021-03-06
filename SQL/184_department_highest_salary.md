# department highest salary

The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.
```
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
```
The Department table holds all departments of the company.
```
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
```
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.
```
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
```

```SQL
# Write your MySQL query statement below
select d.Name as Department, e.Name as Employee, e.Salary as Salary
from Employee as e, Department as d where e.DepartmentId = d.Id
and e.Salary=(Select max(Salary) from Employee e2 where e2.DepartmentId=d.Id)
```
上面的方案速度很慢，再看一个连表查询的：

```sql
select Department.Name as Department,
       Employee.Name as Employee,
       Salary
from Employee join Department on DepartmentId = Department.id
where (DepartmentId, Salary) in
      (select DepartmentId, MAX(distinct Employee.salary) as Salary from Employee group by Employee.DepartmentId)
```
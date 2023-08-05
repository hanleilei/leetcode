## Calculate Special Bonus

Table: Employees

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates the employee ID, employee name, and salary.
```

Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.

The query result format is in the following example.

Example 1:

```
Input:
Employees table:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
Output:
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+
Explanation:
The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
The employee with ID 3 gets 0 bonus because their name starts with 'M'.
The rest of the employees get a 100% bonus.
```

```sql
SELECT employee_id,
    IF (
        employee_id%2
        AND
        name not like "M%", salary, 0
    )
    as bonus
FROM Employees
order by employee_id;
```

下面的这个用到的是 mod，但是似乎有点复杂，用了两个 if

```sql
select
	employee_id,
	if(mod(employee_id, 2) = 1,
		if (left(name, 1)!= 'M', salary, 0),
		0) as bonus
from
	Employees
order by
	employee_id asc
```

受到bard的启发：

```sql
# Write your MySQL query statement below
SELECT
  employee_id,
  CASE
    WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
    ELSE 0
  END AS bonus
FROM employees
ORDER BY employee_id;
```

主要这个是有case语句

再看看Pandas的方法：

```python
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda x: x['salary'] if x['employee_id'] % 2 and not x['name'].startswith('M') else 0,
        axis = 1
    )
    df = employees[['employee_id', 'bonus']].sort_values('employee_id')
    return df
```
# Customers who never order

Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name |
+----+-------+
| 1 | Joe |
| 2 | Henry |
| 3 | Sam |
| 4 | Max |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1 | 3 |
| 2 | 1 |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry |
| Max |
+-----------+

```SQL
# Write your MySQL query statement below
select Name as Customers from Customers where Id not in (select CustomerId from Orders)
```

还有一个用 left join 方法

```SQL
SELECT Customers.Name AS Customers FROM (Customers LEFT JOIN Orders ON Customers.Id = Orders.CustomerId) WHERE Orders.CustomerId IS NULL
```

再来一个，还是left join的方法速度快。

```sql
select c.name as Customers
from Customers c
left join Orders o
on o.customerId = c.id
where o.customerId is NULL
```
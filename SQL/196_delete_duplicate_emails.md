# delete duplicate emails

Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+


```SQL
DELETE P1.*
FROM Person AS p1, Person AS p2
WHERE p1.email = p2.email
AND p1.Id > p2.Id
```

```SQL
# Write your MySQL query statement below
DELETE P1.*
FROM Person AS p1, Person AS p2
WHERE p1.email = p2.email
AND p1.Id > p2.Id
```

下面是一个速度更快的版本，确实快很多。
```SQL
# Write your MySQL query statement below
DELETE
FROM Person
WHERE Id NOT IN
(SELECT Id FROM (SELECT MIN(Id) Id FROM Person GROUP BY Email) p);
```

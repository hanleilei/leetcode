# rising temperature

Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.
```
+---------+------------+------------------+
| Id(INT) | Date(DATE) | Temperature(INT) |
+---------+------------+------------------+
|       1 | 2015-01-01 |               10 |
|       2 | 2015-01-02 |               25 |
|       3 | 2015-01-03 |               20 |
|       4 | 2015-01-04 |               30 |
+---------+------------+------------------+
```
For example, return the following Ids for the above Weather table:
```
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
```

```SQL
# Write your MySQL query statement below
select w1.Id from Weather w1, Weather w2 where w1.Temperature > w2.Temperature and TO_DAYS(w1.DATE)-TO_DAYS(w2.DATE)=1
```

```SQL
SELECT t.id
FROM (SELECT i.*,
             IF(@last_date + interval 1 day = RecordDate and @last_temp < Temperature, 1, 0) AS rownum,
             @last_temp := Temperature,
             @last_date := RecordDate
      FROM (select @last_date := null, @last_temp := null) AS _init
             , Weather i
      ORDER BY i.RecordDate) AS t
WHERE t.rownum = 1;
```

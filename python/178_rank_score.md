Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.
```
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
```
For example, given the above Scores table, your query should generate the following report (order by highest score):
```
+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
```

stepfan大大的方法。。
```SQL
# Write your MySQL query statement below
SELECT
  Score,
  @rank := @rank + (@prev <> (@prev := Score)) Rank
FROM
  Scores,
  (SELECT @rank := 0, @prev := -1) init
ORDER BY Score desc
```

还是用inner join和groupby的方法比较好理解：

```SQL
SELECT Scores.Score, COUNT(Ranking.Score) AS RANK
  FROM Scores
     , (
       SELECT DISTINCT Score
         FROM Scores
       ) Ranking
 WHERE Scores.Score <= Ranking.Score
 GROUP BY Scores.Id, Scores.Score
 ORDER BY Scores.Score DESC;
```

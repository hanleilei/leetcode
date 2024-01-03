# Customers Who Bought All Products

Table: Customer

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
```

This table may contain duplicates rows. 
customer_id is not NULL.
product_key is a foreign key (reference column) to Product table.
 

Table: Product

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
```

product_key is the primary key (column with unique values) for this table.

Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.

Return the result table in any order.

The result format is in the following example.

## Example 1

```text
Input: 
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+
Output: 
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: 
The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.
```

Intuition

To find the customers who have bought all the products, we need to compare the distinct products bought by each customer with the total number of products available. If the counts match, it means the customer has bought all the products.

Approach

Select the customer_id from the Customer table.
Group the results by customer_id.
Apply a HAVING clause to filter out customers who have not bought all the products.
In the HAVING clause, use COUNT(DISTINCT product_key) to count the number of distinct product keys for each customer.

Compare this count with the total count of product keys in the Product table obtained through a subquery.

If the counts match, it means the customer has bought all the products.
Complexity

Time complexity:
The time complexity of this solution depends on the size of the Customer and Product tables. Let's assume there are n customers and m products. The counting of distinct product keys for each customer takes O(n)O(n)O(n) time, and the subquery to count the total number of products takes O(m)O(m)O(m) time. Therefore, the overall time complexity can be approximated as O(n+m)O(n + m)O(n+m).

Space complexity:
The space complexity of this solution is considered O(1)O(1)O(1) or constant. It only requires a constant amount of additional space for storing intermediate results and the subquery. The space usage does not depend on the size of the input tables.

```sql
# Write your MySQL query statement below
select customer_id
from Customer
group by customer_id
having Count(distinct product_key) = (select count(product_key) from Product)
```
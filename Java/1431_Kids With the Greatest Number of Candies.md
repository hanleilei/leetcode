# Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

## Example 1

```text
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
```

## Example 2

```text
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
```

## Example 3

```text
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

## Constraints

```text
n == candies.length
2 <= n <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50
```

注意java的语法，数组和列表的区别：

```text
boolean[] 和 <Boolean> 的区别在于：

类型： boolean[] 是数组类型，而 <Boolean> 是列表类型。
大小： boolean[] 的大小是固定的，而 <Boolean> 的大小可以动态调整。
存储方式： boolean[] 将元素存储在连续的内存空间中，而 <Boolean> 将元素存储在链表中。
```

```java
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max_candies = 0;
        int size = candies.length;
        for(int i = 0; i < size; i++){
            if (candies[i] > max_candies){
                max_candies = candies[i];
            }
        }
        List<Boolean> res = new ArrayList<>();
        for(int j= 0;j < size;j++){
            boolean ans = candies[j] + extraCandies >= max_candies;
            res.add(ans);
        }
        return res;
    }
}
```

# 292 Nim Game

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

###### 开始撸Java的第一题，然而，这个算法time limit exceeded

```java
class Solution {
    public boolean canWinNim(int n) {
        if (n <= 0){
            throw new IllegalArgumentException("");
        }
        Set <Integer> winningNumber = new HashSet<Integer>();
        winningNumber.add(1);
        winningNumber.add(2);
        winningNumber.add(3);

        int i = 4;

        while ( i <= n ) {
            if (!winningNumber.contains(i-1)|| !winningNumber.contains(i -2 ) || !winningNumber.contains(i - 3)){
                winningNumber.add(i);
            }
            i++;
        }
        return winningNumber.contains(n);
    }
}

```
换个思路，其实问题就可以变成这样：
```
1
2
3
4 -> False
5
6
7
8 -> False
```
也就是说，只要这个数字似乎能被4整除，就是false

```Java
class Solution {
    public boolean canWinNim(int n) {
        return n % 4 == 0 ? False: True;
    }
}
```
算是抖个机灵吧。。

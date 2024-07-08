# Pass the Pillow

There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

Example 1:

Input: n = 4, time = 5
Output: 2
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
After five seconds, the 2nd person is holding the pillow.
Example 2:

Input: n = 3, time = 2
Output: 3
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
After two seconds, the 3rd person is holding the pillow.

Constraints:

2 <= n <= 1000
1 <= time <= 1000

```text
Going forward and back to the original position,
take n * 2 - 2 steps.

One loop take n * 2 - 2 steps,
so we can first do time %= (n * 2 - 2) to save the time.

Now we are still at position 1
and it takes n - 1 steps from 1 to n.

If times < n - 1, not reach n yet.
If times > n - 1, will go back from n.

We calculate the distance from n,
which abs(n - 1 - time),
and return n - abs(n - 1 - time).
```

```python
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        return n - abs(n - 1 - time % (n * 2 - 2))
```

# open the lock

[[BFS]]

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:

```text
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
```

Example 2:

```text
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
```

Example 3:

```text
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
```

Example 4:

```text
Input: deadends = ["0000"], target = "8888"
Output: -1
```

Note:

1. The length of deadends will be in the range [1, 500].
2. target will not be in the list deadends.
3. Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.

非常棒的bfs方法，思路也清晰。但是速度感人

```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = set('0000')

        while queue:
            (string, steps) = queue.popleft()
            if string == target:
                return steps
            elif string in dead_set:
                continue
            for i in range(4):
                digit = int(string[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_string = string[:i]+str(new_digit)+string[i+1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps+1))
        return -1
```

再来一个速度快的：

```python
class Solution:
    def openLock(self, deadends, t):
        """
        T: O(1)
        S: O(1)

        - only record the last move, but failed at:
            ["6787", "8778", "7797", "7977", "6877", "7878", "7788", "8787", "6778", "7876", "7687", "7676", "7757", "7768", "7867", "9777", "6776", "7667", "6767", "7775", "7766", "7779", "8877", "6677", "8776", "7887", "7577", "7786", "5777", "7678", "8677", "8767"]
            "7777"

        :type deadends: List[str]
        :type t: str
        :rtype: int
        """
        NOT_FOUND = -1

        if not deadends or not t:
            return NOT_FOUND

        s = '0000'
        dset = set(deadends)

        if s == t:
            return 0
        if s in dset or t in dset:
            return NOT_FOUND

        def dist(u):
            # shortest distance between `u` and '0000'
            return sum(min(int(d), 10 - int(d)) for d in u)

        def nxts(u):
            for i in range(len(u)):
                d = int(u[i])
                pre = u[:i]
                suf = u[i + 1:]
                yield pre + str((d + 1) % 10) + suf
                yield pre + str((d - 1) % 10) + suf

        last_moves = set(nxts(t)) - dset

        if not last_moves:
            return NOT_FOUND

        ans = dist(t)

        for u in last_moves:
            if dist(u) < ans:
                return ans

        return ans + 2
```

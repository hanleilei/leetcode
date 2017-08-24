# Judge route circle

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

##### 很简单，注意别用字典赋值数字的方式实现。还是感觉test case可能太少了，没准过一段时间这种做法就实现不了。

```python
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        from collections import Counter
        d = Counter(moves)
        if d['U'] == d['D'] and d['L'] == d['R']:
            return True
        else:
            return False
```

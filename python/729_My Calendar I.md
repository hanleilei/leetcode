# My Calendar I

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

## Implement the MyCalendar class:

```text
MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
```

## Example 1:

```
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]
```

## Explanation

```text
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
```

## Constraints:

- 0 <= start < end <= 109
- At most 1000 calls will be made to book.

build a tree:

```python
class Node:
    def __init__(self, start, end, left = None, right = None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.bookhelper(self.root, start, end)
    
    def bookhelper(self, root: Node, start: int, end: int, parent=None) -> bool:
        if root:
            if end > root.start and start < root.end:
                return False
            elif end <= root.start:
                return self.bookhelper(root.left, start, end, root)
            else:
                return self.bookhelper(root.right, start, end, root)
        else:
            return self.update(parent, start, end)
    
    def update(self, parent: Node, start: int, end: int) -> None:
        if end <= parent.start:
            parent.left = Node(start, end)
        else: 
            parent.right = Node(start, end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```

binary search:

```python
class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        if end <= start:
            return False
        
        i = bisect.bisect_right(self.intervals, start)
        if i % 2:            # start is in some stored interval
            return False
        
        j = bisect.bisect_left(self.intervals, end)
        if i != j:
            return False
        
        self.intervals[i:i] = [start, end]
        return True
```

# Next Greater Element I

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

#### Example 1:
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
```    
#### Example 2:
```
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
```
### Note:

* All elements in nums1 and nums2 are unique.
* The length of both nums1 and nums2 would not exceed 1000.

先来Stefan大大的算法镇楼：

```python
class Solution:
    def nextGreaterElement(self, findNums: List[int], nums: List[int]) -> List[int]:
        return [next((y for y in nums[nums.index(x):] if y > x), -1) for x in findNums]
```

```python
class Solution:
    def nextGreaterElement(self, findNums: List[int], nums: List[int]) -> List[int]:
        st, d = [], {}
        for n in nums:
            while st and st[-1] < n:
                d[st.pop()] = n
            st.append(n)

        return [d.get(x, -1) for x in findNums]
```

上面的算法虽然都很好理解，但是，速度太慢，下面这个速度ok：

```python
class Solution:
    def nextGreaterElement(self, findNums: List[int], nums: List[int]) -> List[int]:
        stack = []
        mapping = {}
        for num in nums:
            if len(stack) == 0:
                stack.append(num)
            if num > stack[-1]:
                while stack and num > stack[-1]:
                    val = stack.pop()
                    mapping[val] = num
                stack.append(num)
            else:
                stack.append(num)
        while stack:
            val = stack.pop()
            mapping[val] = -1

        for num in findNums:
            stack.append(mapping[num])
        return stack
 
```

# Sort Integers by The Number of 1 Bits

You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

## Example 1

```text
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
```

## Example 2

```text
Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.
```

## Constraints

1 <= arr.length <= 500
$0 <= arr[i] <= 10^4$

直接用lambda。。

```python
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
```

或者用比较啰嗦的：

```python
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = defaultdict(list)
        for i in arr:
            c = bin(i).count("1")
            d[c].append(i)
        
        res = list()
        for j in sorted(d.keys()):
            res += sorted(d[j])
        return res
```

```cpp
class Solution {
public:
    int HammingWeight(int x){ //Brian Kerninghan's Algorithm
        int wt=0;
        while(x>0)
            x&=(x-1), wt++;
        return wt;
    }
    vector<int> sortByBits(vector<int>& arr) {
        vector<vector<int>> B(32);
        for(int x :arr)
            B[HammingWeight(x)].push_back(x);

        for (auto& b: B)
            sort(b.begin(), b.end());
        int count=0;
        for(int i=0; i<32; i++)
            for(int x: B[i])
                arr[count++]=x;
        return arr;
    }
};
```

```cpp
// variant using C++20 popcount
class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), 
        [](unsigned x, unsigned y){
            return popcount(x)==popcount(y)?x<y
            : popcount(x)<popcount(y);
        });
        return arr;
    }
};
```

```cpp
class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), 
        [](int x, int y){
            if (bitset<31>(x).count()==bitset<31>(y).count())
                return x<y;
            else 
                return bitset<31>(x).count()<bitset<31>(y).count();
        });
        return arr;
    }
};
```

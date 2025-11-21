# Product of the Last K Numbers

Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

## Example

### Input

["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

### Output

[null,null,null,null,null,null,20,40,0,null,32]

### Explanation

```text
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
```

## Constraints

```text
0 <= num <= 100
1 <= k <= 4 * 104
At most 4 * 104 calls will be made to add and getProduct.
The product of the stream at any point in time will fit in a 32-bit integer.
```

Follow-up: Can you implement both GetProduct and Add to work in O(1) time complexity instead of O(k) time complexity?

```python
class ProductOfNumbers:
    # 前缀积数组
    # preProduct[i] / preProduct[j] 就是 [i, j] 之间的元素积
    def __init__(self):
        # 初始化放一个 1，便于计算后续添加元素的乘积
        self.preProduct = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # 如果添加的元素是 0，则前面的元素积都废了
            self.preProduct = [1]
            return
        # 前缀积数组中每个元素
        self.preProduct.append(self.preProduct[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.preProduct):
            # 不足 k 个元素，是因为最后 k 个元素存在 0
            return 0
        # 计算最后 k 个元素积
        return self.preProduct[-1] // self.preProduct[-k-1]
```

```c++
class ProductOfNumbers {
public:
    ProductOfNumbers() {
        
    }
    vector<int> A = {1};
    
    void add(int num) {
        if (num)
            A.push_back(A.back() * num);
        else
            A = {1};
    }
    
    int getProduct(int k) {
        return k < A.size() ? A.back() / A[A.size() - k - 1] : 0;
    }
};
```

```java
class ProductOfNumbers {

    ArrayList<Integer> A = new ArrayList(){{
        add(1);
    }};

    public void add(int a) {
        if (a > 0) {
            A.add(A.get(A.size() - 1) * a);
        }
        else {
            A = new ArrayList();
            A.add(1);
        }
    }

    public int getProduct(int k) {
        int n = A.size();
        return k < n ? A.get(n - 1) / A.get(n - k - 1)  : 0;
    }
}
```

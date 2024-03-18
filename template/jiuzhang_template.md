# 面试常考算法模板

## 万能算法小抄 Cheat Sheet V5.0

## 前言

- 版权归属：九章算法（杭州）科技有限公司

- 九章算法是 IT 求职领域领先的互联网在线教育平台。已帮助 30000+求职者获得了 Google、Facebook、阿里巴巴、腾讯、字节跳动等顶尖互联网公司的工作机会。已开设 算法、大数据、人工智能、系统设计、简历提升、模拟面试等方面的课程和服务，致力于 提供高品质、全方位的技术培训和就业指导。

- 可以原文转载和分享，转载时需保留此版权信息，不得对内容进行增删和修改

- 本文作者：九章算法令狐冲

- 官方网站：http://www.jiuzhang.com/

## 目录

前言 ................................................................................................................... 1

二分法 Binary Search ................................................................................................... 3

双指针 Two Pointers .................................................................................................... 8

排序算法 Sorting ....................................................................................................... 17

二叉树分治 Binary Tree Divide & Conquer ................................................................................ 23

二叉搜索树非递归 BST Iterator ........................................................................................... 26

宽度优先搜索 BFS ....................................................................................................... 30

深度优先搜索 DFS ....................................................................................................... 40

动态规划 Dynamic Programming ........................................................................................... 42

堆 Heap ............................................................................................................... 47

并查集 Union Find ...................................................................................................... 52

字典树 Trie ............................................................................................................ 61

LRU 缓存 ............................................................................................................... 66

## 二分法 Binary Search

### 使用条件

• 排序数组 (30-40%是二分)

• 当面试官要求你找一个比 O(n) 更小的时间复杂度算法的时候(99%)

• 找到数组中的一个分割位置，使得左半部分满足某个条件，右半部分不满足(100%)

• 找到一个最大/最小的值使得某个条件被满足(90%)

### 复杂度

• 时间复杂度：O(logn)

• 空间复杂度：O(1)

### 领扣例题

• LintCode 14. 二分查找(在排序的数据集上进行二分)

• LintCode 460. 在排序数组中找最接近的 K 个数 (在未排序的数据集上进行二分)

• LintCode 437. 书籍复印(在答案集上进行二分 )

### 代码模版

```java
int binarySearch(int[] nums, int target) {
    // corner case 处理
    if (nums == null || nums.length == 0) {
        return -1;
    }
    int start = 0, end = nums.length - 1;

    // 要点 1: start + 1 < end
    while (start + 1 < end) {
        // 要点 2：start + (end - start) / 2
        int mid = start + (end - start) / 2;

        // 要点 3：=, <, > 分开讨论，mid 不 +1 也不 -1
        if (nums[mid] == target){
            return mid;
        }
        else if(nums[mid] < target){
            start = mid;
        }
        else{
            end = mid;
        }
    }
    return -1;

```

```python
def binary_search(self, nums, target):
    # corner case 处理

    # 这里等价于 nums is None or len(nums) == 0
    if not nums:
        return -1

    start, end = 0, len(nums) - 1

    # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环
    # 在 first position of target 的情况下不会出现死循环
    # 但是在 last position of target 的情况下会出现死循环
    # 样例：nums=[1，1] target = 1
    # 为了统一模板，我们就都采用 start + 1 < end，就保证不会出现死循环

    while start + 1 < end:
        # python 没有 overflow 的问题，直接 // 2 就可以了
        # java 和 C++ 最好写成 mid = start + (end - start) / 2
        # 防止在 start = 2^31 - 1, end = 2^31 - 1 的情况下出现加法 overflow
        mid = (start + end) // 2
        # > , =, < 的逻辑先分开写，然后在看看 = 的情况是否能合并到其他分支里
        if nums[mid] < target:
            start = mid
        elif nums[mid] == target:
            end = mid
        else:
            end = mid

        # 因为上面的循环退出条件是 start + 1 < end
        # 因此这里循环结束的时候，start 和 end 的关系是相邻关系（1 和 2，3 和 4 这种）
        # 因此需要再单独判断 start 和 end 这两个数谁是我们要的答案
        # 如果是找 first position of target 就先看 start，否则就先看 end

    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1
```

## 双指针 Two Pointers

### 使用条件

• 滑动窗口 (90%)

• 时间复杂度要求 O(n) (80%是双指针)

• 要求原地操作，只可以使用交换，不能使用额外空间 (80%)

• 有子数组 subarray /子字符串 substring 的关键词 (50%)

• 有回文 Palindrome 关键词(50%)

### 复杂度

• 时间复杂度：O(n) ￮ 时间复杂度与最内层循环主体的执行次数有关 ￮ 与有多少重循环无关

• 空间复杂度：O(1) ￮ 只需要分配两个指针的额外内存

### 领扣例题

• LintCode 1879. 两数之和 VII(同向双指针)

• LintCode1712.和相同的二元子数组(相向双指针)

• LintCode627. 最长回文串 (背向双指针)

• LintCode 64: 合并有序数组

### 代码模版

```java
// 相向双指针(patition in quicksort)
public void partition(int[] A, int start, int end){
    if (start >= end){
        return;
    }
    int left = start, right = end;
    // key point 1: pivot is the value, not the index

    int povit = A[(start + end)/2];

    // key point 2: every time you compare left & right, it should be left <= right not left < right

    while (left <= right){
        while(left <= right && A[left] < pivot){
            left++;
        }
        while (left <= right && A[right] > pivot){
            right--;
        }
        if (left <= right){
            int temp = A[Left];
            A[Left] = A[right];
            A[right] = temp;
            left++;
            right--;
        }
    }
}
```

```java
// 背向双指针
left = position;
right = position + 1;
while (left >= 0 && right < length>){
    if(可以停下来){
        break;
    }
    left--;
    right++;
}
```

```java
// 同向双指针
int j = 0;
for( int i = 0; i < n; i++){

}
```

```python

```

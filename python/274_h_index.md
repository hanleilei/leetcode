# H-index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:
```
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
     received 3, 0, 6, 1, 5 citations respectively.
     Since the researcher has 3 papers with at least 3 citations each and the remaining 
     two with no more than 3 citations each, her h-index is 3.
```
Note: If there are several possible values for h, the maximum one is taken as the h-index

不排序：

```Python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0] * (n + 1)  # papers[i] is the number of papers with i citations.
        for c in citations:
            papers[min(n, c)] += 1  # All papers with citations larger than n is count as n.
        i = n
        s = papers[n]  # sum of papers with citations >= i
        while i > s:
            i -= 1
            s += papers[i]
        return ia
```

单行，但是排序：

```Python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))
```

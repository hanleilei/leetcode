class Solution:
    def numsSameConsecDiff(self, n, k):# int, k: int) -> List[int]:
        import collections
        init = [str(i) for i in range(1, 10)]

        dq = collections.deque(init)
        i = 1
        while i <= n:
            num = dq.popleft()                
            if 10 ** (i - 1)<= int(num) + k < 10 ** i:
                dq.append(num + str(int(num) + k))
            if 10 ** (i - 1) <= int(num) - k < 10 ** i:
                dq.append(num + str(int(num) - k))
            i += 1
        return dq
    
n = 3
k = 7

s = Solution()
s.numsSameConsecDiff(n, k)
# # 






# You run a successful software consulting business, and you've just gotten a visit from Earl, 
# who runs the local library. He's looking for software that will help him manage his very peculiar checkout process.

# "Organizing books is hard," says Earl. "I gave up on it years ago.
# Nowadays when you come into the library and ask for a book in a particular genre, 
# I just give you the last book anybody checked in that belongs to that genre."

# "You give people the last book that came in?" you ask.

# "Yeah; it's easy that way, because I can just keep a pile of books near the front."

# "But what do you do if they want a different book?"

# "You can't get cable in this town, so most people aren't so picky. 
# I do like to do some reading on my own inside the library, 
# though, so I instituted a new process. When you check a book in, you give it a rating.
# Every once in a while I want to know the book that was rated the highest in the genre by the last person to check it in."

# After talking it through with Earl, you agree to implement the following interface:

#   * checkOutBook: This function returns the book that was last checked in inside a particular genre, 
#     and removes it from the Library's store.

#   * checkInBook: This function allows the customer to return a book. That book becomes the last one 
#     checked into the genre. It also takes a rating between 1 and 100 (inclusive) so that Earl can figure out which the best books are.

#   * peekHighestRatedBook: This function returns the highest-rated book that is currently checked into 
#     a given genre. It does not change its order in the check-in and -out process.

# Earl and you agree that you can manage storage in memory without worrying about persisting it to disk.

# Please build a class implementing the Library interface below, and a set of tests sufficient to demonstrate correctness. 
# Make sure that you implement all three methods (checkOutBook, checkInBook, highestRatedBook). 
# In the comments attached to each function, please indicate the time and space complexity of the method, 
# and document any unusual edge cases or problems.

# import collections

# class BookStore():
#     def __init__(self) -> None:
#         self.HighestRated = collections.defaultdict()
#         self.genre = collections.defaultdict(list)

#     def checkInBook(self, bookname, genre, rate):
#         rate = int(rate)
#         if rate > 100:
#             rate = 100
#         if rate < 1:
#             rate = 1
            
#         self.genre[genre].append({
#             "name": bookname,
#             "rate": rate
#             })
#         if genre not in self.HighestRated:
#             self.HighestRated[genre]={"rate" : rate, "book" : bookname}
#         if rate > self.HighestRated[genre]["rate"]:
#             self.HighestRated[genre]["rate"] = rate
#             self.HighestRated[genre]["book"] = bookname
        
    
#     def checkOutBook(self, genre):
#         if len(self.genre[genre]) > 0:
#             return self.genre[genre].pop()
#         return -1
    
#     def peekHighestRatedBook(self, genre):
#         return self.HighestRated[genre]
    

# bs = BookStore()
# bs.checkInBook("janeLove", 'novel', "40")
# bs.checkInBook("harryporter", 'novel', "80")
# print(bs.peekHighestRatedBook("novel"))
# # print(bs.checkOutBook("novel"))


# class Solution:
#     def reverseVowels(self, s):# str) -> str:
#         res = list()
#         vowels = "aeiouAEIOU"

#         target_vowels = [i for i in s if i in vowels]

#         for i in s:
#             if i in target_vowels:
#                 res.append(target_vowels.pop())
#             else:
#                 res.append(i)
#         return "".join(res)
    
# s = Solution()
# s.reverseVowels("hello")

# class Solution:
#     def maximumSubarraySum(self, nums, k):# List[int], k: int) -> int:
#         res = 0
#         i = 0
#         t = sum(nums[:k])
#         s = set(nums[:k])

#         while i < len(nums) -k:
#             if len(s) == k:
#                 res = max(res, t)
#             s.remove(nums[i])
#             t = t - nums[i] + nums[i + k]
#             s.add(nums[i + k])
            
                
#             i += 1
#         return res

# s = Solution()
# # nums = [1,1,1,7,8,9]
# nums = [5,3,3,1,1]
# k = 3
# s.maximumSubarraySum(nums, k)

# class Solution:
#     def setZeroes(self, matrix):# List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         zeros = [[i, j] for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == 0]
#         cols = set([i[1] for i in zeros])
#         rows = set([i[0] for i in zeros])
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if i in rows or j in cols:
#                     matrix[i][j] = 0
                    
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# s = Solution()
# print(s.setZeroes(matrix))

# class Solution:
#     def makeGood(self, s):# str) -> str:
#         stack = []
#         for c in s:
#             if stack and stack[-1] == c.swapcase():
#                 stack.pop()
#             else:
#                 stack.append(c)

#         return "".join(stack)
    
# s = Solution()
# n = "kkdsFuqUfSDKK"
# # n = "leEeetcode"
# # n = "abBAcC"
# # n = "s"
# print(s.makeGood(n))

# class Solution:
#     def removeDuplicates(self, nums):# List[int]) -> int:
#         left, right = 0, 1

#         while right < len(nums):
#             if nums[left] < nums[right]:
#                 left += 1
#                 nums[left] = nums[right]
#             right += 1
#         return nums

# nums  = [0,0,1,1,1,2,2,3,3,4]
# s = Solution()
# s.removeDuplicates(nums)
# class Solution:
#     def maxPalindromes(self, s, t):# str, t: int) -> int:
#         m = dict()
#         n = len(s)
        
#         R = [[0 for x in range(n+1)] for x in range(2)]
#         s = "@" + s + "#"
 
#         for j in range(2):
#             rp = t // 2   # length of 'palindrome radius'
#             R[j][0] = 0

#             i = 1
#             while i <= n:

#                 # Attempt to expand palindrome centered at i
#                 while s[i - rp - 1] == s[i + j + rp]:
#                     rp += 1 # Incrementing the length of palindromic
#                             # radius as and when we find valid palindrome

#                 # Assigning the found palindromic length to odd/even
#                 # length array
#                 R[j][i] = rp
#                 k = 1
#                 while (R[j][i - k] != rp - k) and (k < rp):
#                     R[j][i+k] = min(R[j][i-k], rp - k)
#                     k += 1
#                 rp = max(rp - k, 0)
#                 i += k

#         # remove guards
#         s = s[1:len(s)-1]

 
#     # Put all obtained palindromes in a hash map to
#     # find only distinct palindrome
#         m[s[0]] = 1
#         for i in range(1,n):
#             for j in range(2):
#                 for rp in range(R[j][i],0,-1):
#                     m[s[i - rp - 1 : i - rp - 1 + 2 * rp + j]] = 1
#             m[s[i]] = 1
#         return len([i for i in m.keys() if len(i) >= t])

# s = Solution()
# q = "fttfjofpnpfydwdwdnns"
# t = 2
# print(s.maxPalindromes(q, t))

# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         res = 0
#         left = 0

#         while left < len(arr):
#             res += arr[left]

#             right = left + 1

#             while right < len(arr):
#                 res += min(res, arr[right])
#                 right += 1
#             left += 1
#         return res

# s = Solution()
# arr = [3,1,2,4]
# s.sumSubarrayMins(arr)

# from collections import Counter
# class Solution:
#     def numberOfArithmeticSlices(self, A):# List[int]) -> int:
#         total, n = 0, len(A)
#         dp = [Counter() for item in A]
#         for i in range(n):
#             for j in range(i):
#                 dp[i][A[i] - A[j]] += (dp[j][A[i] - A[j]] + 1)      
#             total += sum(dp[i].values())

#         return total - (n-1)*n//2   
    
# A = [3,1,2,4]
# s = Solution()
# s.numberOfArithmeticSlices(A)


# from collections import Counter, defaultdict
# class Solution:
#     def cust_sort(self , input, k):#: List[str], k: int) -> List[str]:
#         # write code here
#         c = Counter(input)
#         d = defaultdict(list)
#         res = list()
        
#         for i, v in c.items():
#             d[v].append(i)

        
#         for i in sorted(d.keys(), reverse=True)[:k]:
#             res.extend(sorted(d[i]))
#         return res


# # inp = ["i","love","hiretual","i","love","coding", "i", "i", "i", "i","love","love","love",]
# inp = ["i","love","hiretual","i","love","coding", "i", "i", "i", "love", "love"]
# k = 3
# s = Solution()
# print(s.cust_sort(inp, k))

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        size = len(nums)
        res = list()
        left = nums[0]
        i = 0

        while i < len(nums)-1:
            res.append(abs(left// (i + 1) - (total - left) // (size - i - 1)))
            left += nums[i+1]
            i += 1
        res.append(total//size)
        m = min(res)
        return res.index(m)
    
s = Solution()
nums = [2,5,3,9,5,3]
s.minimumAverageDifference(nums)





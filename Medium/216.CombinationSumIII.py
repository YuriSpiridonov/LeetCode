"""
    Find all possible combinations of k numbers that add up to a number n, 
    given that only numbers from 1 to 9 can be used and each combination should 
    be a unique set of numbers.

    Note:
        - All numbers will be positive integers.
        - The solution set must not contain duplicate combinations.

    Example:
    Input: k = 3, n = 7
    Output: [[1,2,4]]

    Example:
    Input: k = 3, n = 9
    Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
#Difficulty: Medium
#18 / 18 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.8 MB

#Runtime: 32 ms, faster than 68.72% of Python3 online submissions for Combination Sum III.
#Memory Usage: 13.8 MB, less than 62.64% of Python3 online submissions for Combination Sum III.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return
        self.result = []
        self.backtracking(k, n)
        return self.result

    def backtracking(self, k, n, start = 1, summ = 0, count = 0, nums = []):
        if count > k:
            return
        if count == k and summ == n:
            result = []
            result.extend(nums)
            self.result.append(result)
            return
        for num in range(start, 10):
            if summ + num > n:
                break
            nums.append(num)
            self.backtracking(k, n, num+1, summ+num, count+1, nums)
            nums.pop()

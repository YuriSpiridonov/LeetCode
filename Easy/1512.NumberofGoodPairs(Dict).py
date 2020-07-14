"""
    Given an array of integers nums.
    A pair (i,j) is called good if nums[i] == nums[j] and i < j.
    Return the number of good pairs.

    Example:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

    Constraints:
        - 1 <= nums.length <= 100
        - 1 <= nums[i] <= 100
"""
#Difficulty: Easy
#48 / 48 test cases passed.
#Runtime: 40 ms
#Memory Usage: 13.9 MB

#Runtime: 40 ms, faster than 66.67% of Python3 online submissions for Number of Good Pairs.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        s = set()
        for i, n in enumerate(nums):
            if n in d:
                d[n].append(i)
            else:
                d[n] = [i]
        for value in d.values():
            l = len(value)
            i = 0
            j = 1
            if l > 1:
                while i < l-1:
                    if j == l:
                        i += 1
                        j = min(i + 1, l-1)
                    if i == j:
                        break
                    s.add((value[i], value[j]))
                    j += 1 
        return len(s)

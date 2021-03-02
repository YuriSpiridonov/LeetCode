'''
    You have a set of integers s, which originally contains 
    all the numbers from 1 to n. Unfortunately, due to some 
    error, one of the numbers in s got duplicated to another 
    number in the set, which results in repetition of one 
    number and loss of another number.

    You are given an integer array nums representing the 
    data status of this set after the error.

    Find the number that occurs twice and the number that is 
    missing and return them in the form of an array.

    Example:
    Input: nums = [1,2,2,4]
    Output: [2,3]

    Example:
    Input: nums = [1,1]
    Output: [1,2]

    Constraints:
        - 2 <= nums.length <= 10^4
        - 1 <= nums[i] <= 10^4
'''
#Difficulty: Easy
#49 / 49 test cases passed.
#Runtime: 204 ms
#Memory Usage: 15.8 MB

#Runtime: 204 ms, faster than 56.13% of Python3 online submissions for Set Mismatch.
#Memory Usage: 15.8 MB, less than 60.76% of Python3 online submissions for Set Mismatch.

from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = Counter(nums)
        return [num for num, count in nums.items() if count==2][0], [num for num in range(1, n+1) if not nums[num]][0]

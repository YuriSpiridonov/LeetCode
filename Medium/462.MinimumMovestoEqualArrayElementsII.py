'''
    Given an integer array nums of size n, return the 
    minimum number of moves required to make all array 
    elements equal.

    In one move, you can increment or decrement an element 
    of the array by 1.

    Example:
    Input: nums = [1,2,3]
    Output: 2
    Explanation: Only two moves are needed (remember each 
                 move increments or decrements one element):
                 [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

    Example:
    Input: nums = [1,10,2,9]
    Output: 16

    Constraints:
        - n == nums.length
        - 1 <= nums.length <= 10^5
        - -10^9 <= nums[i] <= 10^9
'''
#Difficulty: Medium
#30 / 30 test cases passed.
#Runtime: 68 ms
#Memory Usage: 15.4 MB

#Runtime: 68 ms, faster than 88.44% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
#Memory Usage: 15.4 MB, less than 43.75% of Python3 online submissions for Minimum Moves to Equal Array Elements II.

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums)//2]
        return sum(abs(num-median) for num in nums)

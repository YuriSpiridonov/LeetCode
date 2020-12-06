"""
    Given a circular array (the next element of the last element is 
    the first element of the array), print the Next Greater Number 
    for every element. The Next Greater Number of a number x is the 
    first greater number to its traversing-order next in the array, 
    which means you could search circularly to find its next greater 
    number. If it doesn't exist, output -1 for this number.

    Example:
    Input: [1,2,1]
    Output: [2,-1,2]
    Explanation: The first 1's next greater number is 2;
	               The number 2 can't find next greater number;
	               The second 1's next greater number needs to 
                 search circularly, which is also 2.

    Note: The length of given array won't exceed 10000.
"""
#Difficulty: Medium
#224 / 224 test cases passed.
#Runtime: 3468 ms
#Memory Usage: 15.8 MB

#Runtime: 3468 ms, faster than 10.47% of Python3 online submissions for Next Greater Element II.
#Memory Usage: 15.8 MB, less than 39.94% of Python3 online submissions for Next Greater Element II.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums += nums
        for i in range(length):
            for j in range(i, i+length):
                if nums[i] < nums[j]:
                    nums[i] = nums[j]
                    break
            else:
                nums[i] = -1
        return nums[:length]

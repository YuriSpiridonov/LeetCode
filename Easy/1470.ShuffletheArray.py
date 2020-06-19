"""
    Given the array nums consisting of 2n elements in the form 
    [x1,x2,...,xn,y1,y2,...,yn].
    
    Return the array in the form [x1,y1,x2,y2,...,xn,yn].
    
    Example:
    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7] 
    Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is 
                 [2,3,5,4,1,7].
    
    Constraints:
        - 1 <= n <= 500
        - nums.length == 2n
        - 1 <= nums[i] <= 10^3
"""
#Difficulty: Easy
#53 / 53 test cases passed.
#Runtime: 56 ms
#Memory Usage: 13.9 MB

#Runtime: 56 ms, faster than 95.78% of Python3 online submissions for Shuffle the Array.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Shuffle the Array.

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle = []
        for num in zip(nums[:n], nums[n:]):
            shuffle += list(num)
        return shuffle

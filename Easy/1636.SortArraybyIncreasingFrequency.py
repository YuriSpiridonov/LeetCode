"""
    Given an array of integers nums, sort the array in increasing order based 
    on the frequency of the values. If multiple values have the same frequency, 
    sort them in decreasing order.

    Return the sorted array.

    Example:
    Input: nums = [1,1,2,2,2,3]
    Output: [3,1,1,2,2,2]
    Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' 
                 has a frequency of 3.

    Example:
    Input: nums = [2,3,1,3,2]
    Output: [1,3,3,2,2]
    Explanation: '2' and '3' both have a frequency of 2, so they are sorted 
                 in decreasing order.

    Example:
    Input: nums = [-1,1,-6,4,5,-6,1,4,1]
    Output: [5,-1,4,4,-6,-6,1,1,1]

    Constraints:
        - 1 <= nums.length <= 100
        - -100 <= nums[i] <= 100
"""
#Difficulty: Easy
#180 / 180 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.1 MB

#Runtime: 40 ms, faster than 98.99% of Python3 online submissions for Sort Array by Increasing Frequency.
#Memory Usage: 14.1 MB, less than 87.39% of Python3 online submissions for Sort Array by Increasing Frequency.

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numbers = set(nums)
        db = {}
        frequency = set()
        result = []
        for num in numbers:
            count = nums.count(num)
            frequency.add(count)
            if count not in db:
                db[count] = []
            db[count].append([num] * count)
        for f in sorted(frequency):
            for vals in sorted(db[f], reverse=True):
                result.extend(vals)
        return result

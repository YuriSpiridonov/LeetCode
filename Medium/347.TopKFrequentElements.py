"""
    Given a non-empty array of integers, return the k most frequent elements.

    Example:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Note:
        - You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
        - Your algorithm's time complexity must be better than O(n log n), where 
          n is the array's size.
        - It's guaranteed that the answer is unique, in other words the set of 
          the top k frequent elements is unique.
        - You can return the answer in any order.
"""
#Difficulty: Medium
#21 / 21 test cases passed.
#Runtime: 112 ms
#Memory Usage: 18.5 MB

#Runtime: 112 ms, faster than 51.73% of Python3 online submissions for Top K Frequent Elements.
#Memory Usage: 18.5 MB, less than 8.25% of Python3 online submissions for Top K Frequent Elements.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d.keys():
                d[num] += 1
            else:
                d[num] = 1
        return [key[0] for key in sorted(d.items(), key=lambda item: item[1])][-k:]

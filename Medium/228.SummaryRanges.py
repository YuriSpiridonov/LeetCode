"""
    Given a sorted integer array without duplicates, return the summary of its 
    ranges.

    Example:
    Input:  [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

    Example:
    Input:  [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
#Difficulty: Medium
#28 / 28 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.6 MB

#Runtime: 32 ms, faster than 64.40% of Python3 online submissions for Summary Ranges.
#Memory Usage: 13.6 MB, less than 95.74% of Python3 online submissions for Summary Ranges.

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        flag = False
        start = None
        end = None
        length = len(nums)
        i = 0
        j = i + 1
        while i < length:
            start = nums[i]
            if j < length:
                end = nums[j]
            if end and end - 1 == start:
                flag = not flag
                end = nums[j]
                j += 1
                while j < length and nums[j] - 1 == nums[j-1]:
                    end = nums[j]
                    j += 1
            if flag:
                ranges.append(str(start)+'->'+str(end))
                i = j
                j = i + 1
                flag = not flag
                continue
            else:
                ranges.append(str(start))
            i += 1
            j = i + 1
        return ranges 

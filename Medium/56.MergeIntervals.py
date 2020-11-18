"""
    Given a collection of intervals, merge all overlapping intervals.

    Example:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into 
                 [1,6].

    NOTE: input types have been changed on April 15, 2019. Please reset to 
          default code definition to get new method signature.
"""
#Difficulty: Medium
#169 / 169 test cases passed.
#Runtime: 100 ms
#Memory Usage: 15.6 MB

#Runtime: 100 ms, faster than 28.72% of Python3 online submissions for Merge Intervals.
#Memory Usage: 15.6 MB, less than 6.52% of Python3 online submissions for Merge Intervals.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][-1]:
                intervals[i-1] = [min(intervals[i][0], intervals[i-1][0]), max(intervals[i][-1], intervals[i-1][-1])]
                intervals.pop(i)
            else:
                i += 1
        return intervals

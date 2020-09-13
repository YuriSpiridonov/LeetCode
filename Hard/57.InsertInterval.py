"""
    Given a set of non-overlapping intervals, insert a new interval into the 
    intervals (merge if necessary).
    You may assume that the intervals were initially sorted according to their 
    start times.

    Example:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

    Example:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

    NOTE: input types have been changed on April 15, 2019. Please reset to 
          default code definition to get new method signature.
"""
#Difficulty: Hard
#154 / 154 test cases passed.
#Runtime: 84 ms
#Memory Usage: 17 MB

#Runtime: 84 ms, faster than 72.13% of Python3 online submissions for Insert Interval.
#Memory Usage: 17 MB, less than 92.34% of Python3 online submissions for Insert Interval.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        length = len(intervals)
        result = []
        while i < length and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < length and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        result.append(newInterval)
        while i < length:
            result.append(intervals[i])
            i += 1
        return result

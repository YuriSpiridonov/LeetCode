"""
    Given a list of intervals, remove all intervals that are covered by another 
    interval in the list.
    Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
    After doing so, return the number of remaining intervals.

    Example:
    Input: intervals = [[1,4],[3,6],[2,8]]
    Output: 2
    Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

    Example:
    Input: intervals = [[1,4],[2,3]]
    Output: 1

    Example:
    Input: intervals = [[0,10],[5,12]]
    Output: 2

    Example:
    Input: intervals = [[3,10],[4,10],[5,11]]
    Output: 2

    Example:
    Input: intervals = [[1,2],[1,4],[3,4]]
    Output: 1

    Constraints:
        - 1 <= intervals.length <= 1000
        - intervals[i].length == 2
        - 0 <= intervals[i][0] < intervals[i][1] <= 10^5
        - All the intervals are unique.
"""
#Difficulty: Medium
#32 / 32 test cases passed.
#Runtime: 572 ms
#Memory Usage: 14.6 MB

#Runtime: 572 ms, faster than 5.06% of Python3 online submissions for Remove Covered Intervals.
#Memory Usage: 14.6 MB, less than 8.91% of Python3 online submissions for Remove Covered Intervals.

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        length = len(intervals)
        while i < length:
            flag = True
            j = i + 1
            while j < length:
                if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                    intervals.pop(i)
                    length -= 1
                    i = max(i-1, 0)
                    if i == 0:
                        flag = False
                elif intervals[i][0] <= intervals[j][0] and intervals[j][1] <= intervals[i][1]:
                    intervals.pop(j)
                    length -= 1
                    i = max(i-1, 0)
                    if i == 0:
                        flag = False
                else:
                    j += 1
            if flag:
                i += 1
        return length

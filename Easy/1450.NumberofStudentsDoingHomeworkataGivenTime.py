"""
    Given two integer arrays startTime and endTime and given an integer 
    queryTime.
    The ith student started doing their homework at the time startTime[i] and 
    finished it at time endTime[i].
    Return the number of students doing their homework at time queryTime. 
    More formally, return the number of students where queryTime lays in the 
    interval [startTime[i], endTime[i]] inclusive.

    Example:
    Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
    Output: 1
    Explanation: We have 3 students where:
                 - The first student started doing homework at time 1 and 
                 finished at time 3 and wasn't doing anything at time 4.
                 - The second student started doing homework at time 2 and 
                 finished at time 2 and also wasn't doing anything at time 4.
                 - The third student started doing homework at time 3 and 
                 finished at time 7 and was the only student doing homework at
                 time 4.
    
    Constraints:
    - startTime.length == endTime.length
    - 1 <= startTime.length <= 100
    - 1 <= startTime[i] <= endTime[i] <= 1000
    - 1 <= queryTime <= 1000             
"""
#Difficulty: Easy
#111 / 111 test cases passed.
#Runtime: 36 ms
#Memory Usage: 13.7 MB

#Runtime: 36 ms, faster than 87.04% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
#Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Number of Students Doing Homework at a Given Time.

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        number_of_students = 0
        for i, start_time in enumerate(startTime):
            if queryTime in range(start_time, endTime[i]+1):
                number_of_students += 1
        return number_of_students

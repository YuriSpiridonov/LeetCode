"""
    Given an array of non-negative integers arr, you are initially positioned 
    at start index of the array. When you are at index i, you can jump to 
    i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

    Notice that you can not jump outside of the array at any time.
    
    Example:
    Input: arr = [4,2,3,0,3,1,2], start = 5
    Output: true
    Explanation: All possible ways to reach at index 3 with value 0 are: 
                 index 5 -> index 4 -> index 1 -> index 3 
                 index 5 -> index 6 -> index 4 -> index 1 -> index 3 

    Example:
    Input: arr = [4,2,3,0,3,1,2], start = 0
    Output: true 
    Explanation: One possible way to reach at index 3 with value 0 is: 
                 index 0 -> index 4 -> index 1 -> index 3

    Example:
    Input: arr = [3,0,2,1,2], start = 2
    Output: false
    Explanation: There is no way to reach at index 1 with value 0.

    Constraints:
        - 1 <= arr.length <= 5 * 10^4
        - 0 <= arr[i] < arr.length
        - 0 <= start < arr.length
"""
#Difficulty: Medium
#54 / 54 test cases passed.
#Runtime: 220 ms
#Memory Usage: 21.1 MB

#Runtime: 220 ms, faster than 46.20% of Python3 online submissions for Jump Game III.
#Memory Usage: 21.1 MB, less than 23.53% of Python3 online submissions for Jump Game III.

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        visited = []
        length = len(arr)
        while queue:
            i = queue.pop(0)
            if arr[i] == 0:
                return True
            if i + arr[i] < length and i + arr[i] not in visited:
                queue.append(i + arr[i])
                visited.append(i)
            if i - arr[i] >= 0 and i - arr[i] not in visited:
                queue.append(i - arr[i])
                visited.append(i)
        return False

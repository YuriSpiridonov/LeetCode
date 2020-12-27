'''
    Given an array of integers arr, you are initially 
    positioned at the first index of the array.

    In one step you can jump from index i to index:
        - i + 1 where: i + 1 < arr.length.
        - i - 1 where: i - 1 >= 0.
        - j where: arr[i] == arr[j] and i != j.

    Return the minimum number of steps to reach the last 
    ndex of the array.

    Notice that you can not jump outside of the array at 
    any time.

    Example:
    Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
    Output: 3
    Explanation: You need three jumps from index 
                 0 --> 4 --> 3 --> 9. Note that index 9 is 
                 the last index of the array.

    Example:
    Input: arr = [7]
    Output: 0
    Explanation: Start index is the last index. You don't 
                 need to jump.

    Example:
    Input: arr = [7,6,9,6,9,6,9,7]
    Output: 1
    Explanation: You can jump directly from index 0 to index 
                 7 which is last index of the array.

    Example:
    Input: arr = [6,1,9]
    Output: 2

    Example:
    Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
    Output: 3

    Constraints:
        - 1 <= arr.length <= 5 * 10^4
        - -10^8 <= arr[i] <= 10^8
'''
#Difficulty: Hard
#28 / 28 test cases passed.
#Runtime: 1224 ms
#Memory Usage: 28.8 MB

#Runtime: 1224 ms, faster than 5.17% of Python3 online submissions for Jump Game IV.
#Memory Usage: 28.8 MB, less than 63.79% of Python3 online submissions for Jump Game IV.

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indices = {}
        visited = set()
        queue = [[0, 0]] # index, step
        length = len(arr)
        for ind, num in enumerate(arr):
            if num not in indices:
                indices[num] = []
            indices[num].append(ind)
        while queue:
            index, steps = queue.pop(0)
            if index == length - 1:
                break
            if indices[arr[index]]:
                for i in indices[arr[index]]:
                    if i not in visited:
                        visited.add(i)
                        queue.append([i, steps+1])
                indices[arr[index]] = []
            if index - 1 > 0 and index - 1 not in visited:
                visited.add(index-1)
                queue.append([index-1, steps+1])
            if index + 1 not in visited:
                visited.add(index+1)
                queue.append([index+1, steps+1])
        return steps

"""
    Given an array target and an integer n. In each iteration, you will read a 
    number from  list = {1,2,3..., n}.
    Build the target array using the following operations:
        - Push: Read a new element from the beginning list, and push it in the 
          array.
        - Pop: delete the last element of the array.
        - If the target array is already built, stop reading more elements.

    You are guaranteed that the target array is strictly increasing, only 
    containing numbers between 1 to n inclusive.
    Return the operations to build the target array.
    You are guaranteed that the answer is unique.

    Example:
    Input: target = [1,3], n = 3
    Output: ["Push","Push","Pop","Push"]
    Explanation: 
        Read number 1 and automatically push in the array -> [1]
        Read number 2 and automatically push in the array then Pop it -> [1]
        Read number 3 and automatically push in the array -> [1,3]

    Constraints:
        - 1 <= target.length <= 100
        - 1 <= target[i] <= 100
        - 1 <= n <= 100
        - target is strictly increasing.
"""
#Difficulty: Easy
#48 / 48 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.8 MB

#Runtime: 28 ms, faster than 90.11% of Python3 online submissions for Build an Array With Stack Operations.
#Memory Usage: 13.8 MB, less than 70.51% of Python3 online submissions for Build an Array With Stack Operations.

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        n = min(n, target[-1]) + 1
        for i in range(1, n):
            operations += ["Push"]
            if i not in target:
                operations += ["Pop"]
        return operations

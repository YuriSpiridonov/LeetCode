"""
    Given a non-empty array of unique positive integers A, consider the 
    following graph:
        - There are A.length nodes, labelled A[0] to A[A.length - 1];
        - There is an edge between A[i] and A[j] if and only if A[i] and A[j] 
          share a common factor greater than 1.

    Return the size of the largest connected component in the graph.

    Example:
    Input: [4,6,15,35]
    Output: 4

    Example:
    Input: [20,50,9,63]
    Output: 2

    Example:
    Input: [2,3,6,7,4,12,21,39]
    Output: 8

    Note:
        1. 1 <= A.length <= 20000
        2. 1 <= A[i] <= 100000
"""
#Difficulty: Hard
#100 / 100 test cases passed.
#Runtime: 2176 ms
#Memory Usage: 19.3 MB

#Runtime: 2176 ms, faster than 81.70% of Python3 online submissions for Largest Component Size by Common Factor.
#Memory Usage: 19.3 MB, less than 60.78% of Python3 online submissions for Largest Component Size by Common Factor.

import math

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        factors = {}
        numbers = list(range(max(A)+1))
        for number in A:
            for factor in range(2, int(math.sqrt(number))+1):
                if not number % factor:
                    self.union(numbers, number, factor)
                    self.union(numbers, number, number // factor)
        for number in A:
            number = self.unionFind(numbers, number)
            if number not in factors:
                factors[number] = 0
            factors[number] += 1
        return max(factors.values())

    def unionFind(self, numbers, number):
        while numbers[number] != number:
            numbers[number] = numbers[numbers[number]]
            number = numbers[number]
        return number

    def union(self, numbers, number, factor):
        if numbers[number] == numbers[factor]:
            return
        new_number = self.unionFind(numbers, number)
        new_factor = self.unionFind(numbers, factor)
        numbers[new_number] = new_factor

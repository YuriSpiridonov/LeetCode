"""
    There are n people, each of them has a unique ID from 0 to n - 1 and each 
    person of them belongs to exactly one group.
    Given an integer array groupSizes which indicated that the person with 
    ID = i belongs to a group of groupSize[i] persons.
    Return an array of the groups where ans[j] contains the IDs of the jth 
    group. Each ID should belong to exactly one group and each ID should be 
    present in your answer. Also if a person with ID = i belongs to group j in 
    your answer, then ans[j].length == groupSize[i] should be true.
    If there is multiple answers, return any of them. It is guaranteed that 
    there will be at least one valid solution for the given input.

    Example:
    Input: groupSizes = [3,3,3,3,3,1,3]
    Output: [[5],[0,1,2],[3,4,6]]
    Explanation: 
                 Other possible solutions are [[2,1,6],[5],[0,4,3]] 
                                          and [[5],[0,6,2],[4,3,1]].

    Example:
    Input: groupSizes = [2,1,3,3,3,2]
    Output: [[1],[0,5],[2,3,4]]

    Constraints:
        - groupSizes.length == n
        - 1 <= n <= 500
        - 1 <= groupSizes[i] <= n
"""
#Difficulty: Medium
#102 / 102 test cases passed.
#Runtime: 72 ms
#Memory Usage: 13.7 MB

#Runtime: 72 ms, faster than 97.63% of Python3 online submissions for Group the People Given the Group Size They Belong To.
#Memory Usage: 13.7 MB, less than 96.74% of Python3 online submissions for Group the People Given the Group Size They Belong To.

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []
        for i, n in enumerate(groupSizes):
            if n not in groups:
                groups[n] = []
            groups[n].append(i)
        for i in groups.keys():
            while groups[i]:
                result.append(groups[i][:i])
                groups[i] = groups[i][i:]
        return result

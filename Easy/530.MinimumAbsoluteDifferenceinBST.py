"""
    Given a binary search tree with non-negative values, find the minimum 
    absolute difference between values of any two nodes.

    Example:
    Input:
           1
            \
             3
            /
           2

    Output:
    1
    Explanation:
    The minimum absolute difference is 1, which is the difference between 2 
    and 1 (or between 2 and 3).

    Note:
        - There are at least two nodes in this BST.
        - This question is the same as 783: 
          https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
#Difficulty: Easy
#186 / 186 test cases passed.
#Runtime: 8264 ms
#Memory Usage: 15.8 MB

#Runtime: 8264 ms, faster than 5.77% of Python3 online submissions for Minimum Absolute Difference in BST.
#Memory Usage: 15.8 MB, less than 70.31% of Python3 online submissions for Minimum Absolute Difference in BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        result = [float(inf)]
        self.preorder(result, root, [float(inf)])
        return result[0]

    def preorder(self, result, root, prev):
        if not root:
            return
        for val in prev:
            dif = abs(root.val - val)
            if dif < result[0]:
                result[0] = dif
        prev.append(root.val)
        self.preorder(result, root.left, prev)
        self.preorder(result, root.right, prev)

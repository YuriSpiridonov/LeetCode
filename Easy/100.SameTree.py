"""
    Given two binary trees, write a function to check if they are the same or 
    not.
    Two binary trees are considered the same if they are structurally identical 
    and the nodes have the same value.

    Example 1:
    Input:     1         1
              / \       / \
             2   3     2   3
    
            [1,2,3],   [1,2,3]
    Output: true

    Example 2:
    Input:     1         1
              /           \
             2             2
    
            [1,2],     [1,null,2]
    Output: false
"""
#Difficulty: Easy
#57 / 57 test cases passed.
#Runtime: 20 ms
#Memory Usage: 14 MB

#Runtime: 20 ms, faster than 98.83% of Python3 online submissions for Same Tree.
#Memory Usage: 14 MB, less than 13.23% of Python3 online submissions for Same Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        result = []
        self.preorder(p, q, result)
        return min(result)

    def preorder(self, p, q, result):
        if not p and not q:
            result.append(True)
            return
        if not p or not q:
            result.append(False)
            return
        if p.val != q.val:
            result.append(False)
        if p.val == q.val:
            result.append(True)
            self.preorder(p.left, q.left, result)
            self.preorder(p.right, q.right, result)

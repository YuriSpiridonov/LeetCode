"""
    A binary tree is univalued if every node in the tree has the same value.
    Return true if and only if the given tree is univalued.

    Example:
            1
           / \
          1   1
         / \   \
        1   1   1

    Input: [1,1,1,1,1,null,1]
    Output: true

    Example:
            2
           / \
          2   2
         / \
        5   2 

    Input: [2,2,2,5,2]
    Output: false

    Note:
        1. The number of nodes in the given tree will be in the range [1, 100].
        2. Each node's value will be an integer in the range [0, 99].
"""
#Difficulty: Easy
#72 / 72 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14 MB

#Runtime: 32 ms, faster than 71.93% of Python3 online submissions for Univalued Binary Tree.
#Memory Usage: 14 MB, less than 6.27% of Python3 online submissions for Univalued Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isUnivalTree(self, root: TreeNode) -> bool:
        result = [True]
        val = root.val
        self.preorder(root, val, result)
        return min(result)

    def preorder(self, root, val, result):
        if not root:
            return 0
        if root.val != val:
            result.append(False)
        self.preorder(root.left, val, result)
        self.preorder(root.right, val, result)

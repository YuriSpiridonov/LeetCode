"""
    Find the sum of all left leaves in a given binary tree.

    Example:

        3
       / \
      9  20
        /  \
       15   7
    There are two left leaves in the binary tree, with values 9 and 15 
    respectively. Return 24.
"""
#Difficulty: Easy
#102 / 102 test cases passed.
#Runtime: 28 ms
#Memory Usage: 14.2 MB

#Runtime: 28 ms, faster than 91.15% of Python3 online submissions for Sum of Left Leaves.
#Memory Usage: 14.2 MB, less than 78.35% of Python3 online submissions for Sum of Left Leaves.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = []
        self.preorder(root, result)
        return sum(result)

    def preorder(self, root, result):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            result.append(root.left.val)
        self.preorder(root.left, result)
        self.preorder(root.right, result)

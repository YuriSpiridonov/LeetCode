"""
    Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
    such that adding up all the values along the path equals the given sum.
    Note: A leaf is a node with no children.

    Example:
    Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1   
    return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
#Difficulty: Easy
#114 / 114 test cases passed.
#Runtime: 44 ms
#Memory Usage: 15.6 MB

#Runtime: 44 ms, faster than 72.99% of Python3 online submissions for Path Sum.
#Memory Usage: 15.6 MB, less than 43.57% of Python3 online submissions for Path Sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def hasPathSum(self, root: TreeNode, summ: int) -> bool:
        result = []
        s = 0
        self.summFunc(root, s, result)
        return True if summ in result else False

    def summFunc(self, root, s, result):
        if not root:
            return 0
        s += root.val
        self.summFunc(root.left, s, result)
        self.summFunc(root.right, s, result)
        if not root.left and not root.right:
            result.append(s)

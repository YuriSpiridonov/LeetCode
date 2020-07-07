"""
    Given a binary tree, return the preorder traversal of its nodes' values.

    Example:
    Input: [1,null,2,3]
           1
            \
             2
            /
           3

    Output: [1,2,3]
    Follow up: Recursive solution is trivial, could you do it iteratively?
"""
#Difficulty: Medium
#68 / 68 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.9 MB

#Runtime: 32 ms, faster than 52.63% of Python3 online submissions for Binary Tree Preorder Traversal.
#Memory Usage: 13.9 MB, less than 26.23% of Python3 online submissions for Binary Tree Preorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        preorder = []
        self.traverse(root, preorder)
        return preorder

    def traverse(self, root, preorder):
        if not root:
            return 0
        preorder.append(root.val)
        self.traverse(root.left, preorder)
        self.traverse(root.right, preorder)

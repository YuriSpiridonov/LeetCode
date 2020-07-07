"""
    Given a binary tree, return the inorder traversal of its nodes' values.

    Example:
    Input: [1,null,2,3]
           1
            \
             2
            /
           3

    Output: [1,3,2]
    Follow up: Recursive solution is trivial, could you do it iteratively?
"""
#Difficulty: Medium
#68 / 68 test cases passed.
#Runtime: 40 ms
#Memory Usage: 13.9 MB

#Runtime: 40 ms, faster than 19.72% of Python3 online submissions for Binary Tree Inorder Traversal.
#Memory Usage: 13.9 MB, less than 27.97% of Python3 online submissions for Binary Tree Inorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []
        self.traverse(root, inorder)
        return inorder
        
    def traverse(self, root, inorder):
        if not root:
            return 0
        self.traverse(root.left, inorder)
        inorder.append(root.val)
        self.traverse(root.right, inorder)

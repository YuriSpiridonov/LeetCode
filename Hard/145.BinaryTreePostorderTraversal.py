"""
    Given a binary tree, return the postorder traversal of its nodes' values.

    Example:
    Input: [1,null,2,3]
           1
            \
             2
            /
           3

    Output: [3,2,1]
    Follow up: Recursive solution is trivial, could you do it iteratively?
"""
#Difficulty: Hard
#68 / 68 test cases passed.
#Runtime: 44 ms
#Memory Usage: 14.1 MB

#Runtime: 44 ms, faster than 14.41% of Python3 online submissions for Binary Tree Postorder Traversal.
#Memory Usage: 14.1 MB, less than 5.40% of Python3 online submissions for Binary Tree Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder = []
        self.traverse(root, postorder)
        return postorder

    def traverse(self, root, postorder):
        if not root:
            return 0
        self.traverse(root.left, postorder)
        self.traverse(root.right, postorder)
        postorder.append(root.val)

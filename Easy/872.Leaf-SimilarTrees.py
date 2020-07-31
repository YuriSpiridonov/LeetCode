"""
    Consider all the leaves of a binary tree.  From left to right order, the 
    values of those leaves form a leaf value sequence.

                 3
               /   \
              5     1
             / \   / \
            6   2 9   8
               / \
              7   4

    For example, in the given tree above, the leaf value sequence is 
    (6, 7, 4, 9, 8).
    Two binary trees are considered leaf-similar if their leaf value sequence 
    is the same.
    Return true if and only if the two given trees with head nodes root1 and 
    root2 are leaf-similar.

    Constraints:
        - Both of the given trees will have between 1 and 200 nodes.
        - Both of the given trees will have values between 0 and 200
"""
#Difficulty: Easy
#38 / 38 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.1 MB

#Runtime: 32 ms, faster than 79.38% of Python3 online submissions for Leaf-Similar Trees.
#Memory Usage: 14.1 MB, less than 6.25% of Python3 online submissions for Leaf-Similar Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        one_leafs = []
        two_leafs = []
        self.preorder(root1, one_leafs)
        self.preorder(root2, two_leafs)
        return one_leafs == two_leafs

    def preorder(self, root, leafs):
        if not root:
            return 0
        if not root.left and not root.right:
            leafs.append(root.val)
        self.preorder(root.left, leafs)
        self.preorder(root.right, leafs)

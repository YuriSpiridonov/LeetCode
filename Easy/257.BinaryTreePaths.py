"""
    Given a binary tree, return all root-to-leaf paths.
    Note: A leaf is a node with no children.

    Example:
    Input:
           1
         /   \
        2     3
         \
          5

    Output: ["1->2->5", "1->3"]
    Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
#Difficulty: Easy
#209 / 209 test cases passed.
#Runtime: 16 ms
#Memory Usage: 13.8 MB

#Runtime: 16 ms, faster than 99.92% of Python3 online submissions for Binary Tree Paths.
#Memory Usage: 13.8 MB, less than 78.79% of Python3 online submissions for Binary Tree Paths.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        path = ''
        self.preorder(root, path, paths)
        return paths

    def preorder(self, root, path, paths):
        if not root:
            return
        path += str(root.val) + '->'
        self.preorder(root.left, path, paths)
        self.preorder(root.right, path, paths)
        if not root.left and not root.right:
            path = path[:-2]
            paths.append(path)

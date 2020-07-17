"""
    Given a binary tree, return the zigzag level order traversal of its nodes' 
    values. (ie, from left to right, then right to left for the next level and 
    alternate between).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
    return its zigzag level order traversal as:
        [
          [3],
          [20,9],
          [15,7]
        ]
"""
#Difficulty: Medium
#33 / 33 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14 MB

#Runtime: 36 ms, faster than 56.05% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
#Memory Usage: 14 MB, less than 69.31% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return root
        queue = [root]
        result = []
        reverse = False
        while queue:
            length = len(queue)
            level = []
            while length:
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                length -= 1
            if reverse:
                result.append(level[::-1])
                reverse = not reverse
            else:
                result.append(level)
                reverse = not reverse
        return result

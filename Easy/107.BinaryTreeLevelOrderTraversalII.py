"""
    Given a binary tree, return the bottom-up level order traversal of its 
    nodes' values. (ie, from left to right, level by level from leaf to root).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
    return its bottom-up level order traversal as:
        [
          [15,7],
          [9,20],
          [3]
        ]
"""
#Difficulty: Easy
#34 / 34 test cases passed.
#Runtime: 32 ms
#Memory Usage: 13.9 MB

#Runtime: 32 ms, faster than 90.65% of Python3 online submissions for Binary Tree Level Order Traversal II.
#Memory Usage: 13.9 MB, less than 89.09% of Python3 online submissions for Binary Tree Level Order Traversal II.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return root
        queue = [root]
        result = []
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
            result.append(level)
        return reversed(result)

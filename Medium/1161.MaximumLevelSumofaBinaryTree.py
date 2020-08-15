"""
    Given the root of a binary tree, the level of its root is 1, the level of 
    its children is 2, and so on.
    Return the smallest level X such that the sum of all the values of nodes at 
    level X is maximal.

    Example:
             1
            / \
           7   0
          / \
         7  -8

    Input: [1,7,0,7,-8,null,null]
    Output: 2
    Explanation: 
                Level 1 sum = 1.
                Level 2 sum = 7 + 0 = 7.
                Level 3 sum = 7 + -8 = -1.
                So we return the level with the maximum sum which is level 2.

    Note:
        1. The number of nodes in the given tree is between 1 and 10^4.
        2. -10^5 <= node.val <= 10^5
"""
#Difficulty: Medium
#34 / 34 test cases passed.
#Runtime: 316 ms
#Memory Usage: 18 MB

#Runtime: 316 ms, faster than 89.30% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
#Memory Usage: 18 MB, less than 69.43% of Python3 online submissions for Maximum Level Sum of a Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [root]
        depth = 0
        level = 0
        summ = 0
        while queue:
            length = len(queue)
            level_sum = 0
            depth += 1
            while length:
                length -= 1
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > summ:
                summ = level_sum
                level = depth
        return level

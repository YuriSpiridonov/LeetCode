"""
    Given a non-empty binary tree, return the average value of the nodes on 
    each level in the form of an array.

    Example:
    Input:
            3
           / \
          9  20
            /  \
           15   7
    Output: [3, 14.5, 11]
    Explanation:
                The average value of nodes on level 0 is 3,  on level 1 is 14.5, 
                and on level 2 is 11. Hence return [3, 14.5, 11].

    Note:
        1. The range of node's value is in the range of 32-bit signed integer.
"""
#Difficulty: Easy
#65 / 65 test cases passed.
#Runtime: 48 ms
#Memory Usage: 15.9 MB

#Runtime: 48 ms, faster than 91.23% of Python3 online submissions for Average of Levels in Binary Tree.
#Memory Usage: 15.9 MB, less than 85.86% of Python3 online submissions for Average of Levels in Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        average = []
        while queue:
            length = len(queue)
            s = 0 # summ
            n = 0 # numbers counter
            while length:
                length -= 1
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                s += node.val
                n += 1
            average.append(s / n)
        return average

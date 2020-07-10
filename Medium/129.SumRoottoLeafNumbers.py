"""
    Given a binary tree containing digits from 0-9 only, each root-to-leaf path 
    could represent a number.
    An example is the root-to-leaf path 1->2->3 which represents the number 123.
    Find the total sum of all root-to-leaf numbers.
    Note: A leaf is a node with no children.

    Example:
    Input: [4,9,0,5,1]

                4
               / \
              9   0
             / \
            5   1
    Output: 1026
    Explanation:
                - The root-to-leaf path 4->9->5 represents the number 495.
                - The root-to-leaf path 4->9->1 represents the number 491.
                - The root-to-leaf path 4->0 represents the number 40.
                - Therefore, sum = 495 + 491 + 40 = 1026.
"""
#Difficulty: Medium
#110 / 110 test cases passed.
#Runtime: 44 ms
#Memory Usage: 13.9 MB

#Runtime: 44 ms, faster than 21.55% of Python3 online submissions for Sum Root to Leaf Numbers.
#Memory Usage: 13.9 MB, less than 63.23% of Python3 online submissions for Sum Root to Leaf Numbers.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        numbers = []
        number = 0
        self.dfs(root, number, numbers)
        return sum(numbers)

    def dfs(self, root, number, numbers):
        if not root:
            return
        number = number * 10 + root.val
        self.dfs(root.left, number, numbers)
        self.dfs(root.right, number, numbers)
        if not root.left and not root.right:
            numbers.append(number)

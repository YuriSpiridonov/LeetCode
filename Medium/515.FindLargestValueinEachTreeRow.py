"""
    You need to find the largest value in each row of a binary tree.

    Example:
    Input: 
              1
             / \
            3   2
           / \   \  
          5   3   9 

    Output: [1, 3, 9]
"""
#Difficulty: Medium
#78 / 78 test cases passed.
#Runtime: 48 ms
#Memory Usage: 16 MB

#Runtime: 48 ms, faster than 80.31% of Python3 online submissions for Find Largest Value in Each Tree Row.
#Memory Usage: 16 MB, less than 61.86% of Python3 online submissions for Find Largest Value in Each Tree Row.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return root
        queue = [root]
        max_in_row = []
        while queue:
            length = len(queue)
            max_num = float(-inf)
            while length:
                length -= 1
                node = queue.pop(0)
                max_num = max(max_num, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_in_row.append(max_num)
        return max_in_row

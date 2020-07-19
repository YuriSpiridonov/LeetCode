"""
    Given a binary tree, imagine yourself standing on the right side of it, 
    return the values of the nodes you can see ordered from top to bottom.

    Example:
    Input: [1,2,3,null,5,null,4]
    Output: [1, 3, 4]
    Explanation:
           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---
"""
#Difficulty: Medium
#211 / 211 test cases passed.
#Runtime: 44 ms
#Memory Usage: 14 MB

#Runtime: 44 ms, faster than 28.97% of Python3 online submissions for Binary Tree Right Side View.
#Memory Usage: 14 MB, less than 9.61% of Python3 online submissions for Binary Tree Right Side View. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        queue = [root]
        right_side_view = []
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
            right_side_view.append(level[-1])
        return right_side_view

"""
    Given two binary search trees root1 and root2.
    Return a list containing all the integers from both trees sorted in 
    ascending order.

    Example:
    Input: root1 = [2,1,4], root2 = [1,0,3]
    Output: [0,1,1,2,3,4]

    Example:
    Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
    Output: [-10,0,0,1,2,5,7,10]

    Example:
    Input: root1 = [], root2 = [5,1,7,0,2]
    Output: [0,1,2,5,7]

    Example:
    Input: root1 = [0,-10,10], root2 = []
    Output: [-10,0,10]

    Example:
    Input: root1 = [1,null,8], root2 = [8,1]
    Output: [1,1,8,8]

    Constraints:
        - Each tree has at most 5000 nodes.
        - Each node's value is between [-10^5, 10^5].
"""
#Difficulty: Medium
#48 / 48 test cases passed.
#Runtime: 344 ms
#Memory Usage: 17.2 MB

#Runtime: 344 ms, faster than 93.25% of Python3 online submissions for All Elements in Two Binary Search Trees.
#Memory Usage: 17.2 MB, less than 76.01% of Python3 online submissions for All Elements in Two Binary Search Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        queue = []
        result = []
        if root1:
            queue.append(root1)
        if root2:
            queue.append(root2)
        while queue:
            length = len(queue)
            while length:
                length -= 1
                node = queue.pop(0)
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return sorted(result)

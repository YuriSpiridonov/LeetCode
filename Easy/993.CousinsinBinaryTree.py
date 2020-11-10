"""
    In a binary tree, the root node is at depth 0, and children of each depth 
    k node are at depth k+1.

    Two nodes of a binary tree are cousins if they have the same depth, but 
    have different parents.

    We are given the root of a binary tree with unique values, and the values 
    x and y of two different nodes in the tree.

    Return true if and only if the nodes corresponding to the values x and y 
    are cousins.

    Example:
             1
            / \
           2   3
          /
         4

    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false

    Example:
             1
            / \
           2   3
            \   \
             4   5

    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true

    Example:
             1
            / \
           2   3
            \
             4

    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false

    Constraints:
        - The number of nodes in the tree will be between 2 and 100.
        - Each node has a unique integer value from 1 to 100.
"""
#Difficulty: Easy
#104 / 104 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14 MB

#Runtime: 36 ms, faster than 33.67% of Python3 online submissions for Cousins in Binary Tree.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Cousins in Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [root]
        while queue:
            p1 = None
            p2 = None
            length = len(queue)
            while length:
                length -= 1
                curr = queue.pop(0)
                if curr:
                    if curr.left and curr.left.val == x or curr.right and curr.right.val == x:
                        p1 = curr
                    if curr.left and curr.left.val == y or curr.right and curr.right.val == y:
                        p2 = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
                if p1 and p2 and p1 != p2:
                    return True
        return False

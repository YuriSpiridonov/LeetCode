'''
    Given the root of a binary tree, then value v and depth 
    d, you need to add a row of nodes with value v at the 
    given depth d. The root node is at depth 1.

    The adding rule is: given a positive integer depth d, 
    for each NOT null tree nodes N in depth d-1, create two 
    tree nodes with value v as N's left subtree root and 
    right subtree root. And N's original left subtree should 
    be the left subtree of the new left subtree root, its 
    original right subtree should be the right subtree of 
    the new right subtree root. If depth d is 1 that means 
    there is no depth d-1 at all, then create a tree node 
    with value v as the new root of the whole original tree, 
    and the original tree is the new root's left subtree.

    Example:
    Input: 
    A binary tree as following:
            4
          /   \
         2     6
        / \   / 
       3   1 5
    v = 1
    d = 2

    Output: 
            4
           / \
          1   1
         /     \
        2       6
       / \     / 
      3   1   5   

    Example:
    Input: 
    A binary tree as following:
            4
           /   
          2    
         / \   
        3   1
    v = 1
    d = 3

    Output: 
            4
           /   
          2
         / \    
        1   1
       /     \  
      3       1

    Note:
        1. The given d is in range [1, maximum depth of the 
           given tree + 1].
        2. The given binary tree has at least one tree node.
'''
#Difficulty: Medium
#109 / 109 test cases passed.
#Runtime: 56 ms
#Memory Usage: 16.2 MB

#Runtime: 56 ms, faster than 64.46% of Python3 online submissions for Add One Row to Tree.
#Memory Usage: 16.2 MB, less than 79.05% of Python3 online submissions for Add One Row to Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        depth = 1
        queue = [root]

        if depth == d:
            left = root
            root = TreeNode(v)
            root.left = left

        while queue or depth <= d:
            length = len(queue)
            depth += 1
            while length:
                length -= 1
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                if depth == d and node:
                    left = node.left
                    right = node.right
                    if left:
                        node.left = TreeNode(v)
                        node.left.left = left
                    if right:
                        node.right = TreeNode(v)
                        node.right.right = right
                    if not node.left:
                        node.left = TreeNode(v)
                    if not node.right:
                        node.right = TreeNode(v)
                else:
                    node = TreeNode(v)
        return root
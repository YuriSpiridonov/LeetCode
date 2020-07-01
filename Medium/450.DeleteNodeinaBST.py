"""
    Given a root node reference of a BST and a key, delete the node with the 
    given key in the BST. Return the root node reference (possibly updated) of 
    the BST.
    Basically, the deletion can be divided into two stages:
    Search for a node to remove.
    If the node is found, delete the node.
    Note: Time complexity should be O(height of tree).

    Example:
    root = [5,3,6,2,4,null,7]
    key = 3

            5
           / \
          3   6
         / \   \
        2   4   7

    Given key to delete is 3. So we find the node with value 3 and delete it.
    One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
    
            5
           / \
          4   6
         /     \
        2       7

    Another valid answer is [5,2,6,null,4,null,7].

            5
           / \
          2   6
           \   \
            4   7
"""
#Difficulty: Medium
#85 / 85 test cases passed.
#Runtime: 68 ms
#Memory Usage: 18.1 MB

#Runtime: 68 ms, faster than 98.17% of Python3 online submissions for Delete Node in a BST.
#Memory Usage: 18.1 MB, less than 9.61% of Python3 online submissions for Delete Node in a BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        current = root
        if current is None:
            return current
        if current.val > key:
            current.left = self.deleteNode(current.left, key)
        elif current.val < key:
            current.right = self.deleteNode(current.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            current = root.right
            while current.left is not None:
                current = current.left
            temp = current
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root

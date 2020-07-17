"""
    Implement an iterator over a binary search tree (BST). Your iterator will 
    be initialized with the root node of a BST.
    Calling next() will return the next smallest number in the BST.

    Example:

            7
           / \
          3  15
            /  \
           9   20

    BSTIterator iterator = new BSTIterator(root);
    iterator.next();    // return 3
    iterator.next();    // return 7
    iterator.hasNext(); // return true
    iterator.next();    // return 9
    iterator.hasNext(); // return true
    iterator.next();    // return 15
    iterator.hasNext(); // return true
    iterator.next();    // return 20
    iterator.hasNext(); // return false

    Note:
        - next() and hasNext() should run in average O(1) time and uses O(h) 
          memory, where h is the height of the tree.
        - You may assume that next() call will always be valid, that is, there 
          will be at least a next smallest number in the BST when next() is 
          called.
"""
#Difficulty: Medium
#62 / 62 test cases passed.
#Runtime: 92 ms
#Memory Usage: 20 MB

#Runtime: 92 ms, faster than 38.46% of Python3 online submissions for Binary Search Tree Iterator.
#Memory Usage: 20 MB, less than 97.86% of Python3 online submissions for Binary Search Tree Iterator.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.inorder(root, self.stack)
        self.stack.reverse()

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.stack:
            return self.stack.pop()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.stack else False

    def inorder(self, root, stack):
        """
        prepare stack
        """
        if not root:
            return 0
        self.inorder(root.left, stack)
        stack.append(root.val)
        self.inorder(root.right, stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

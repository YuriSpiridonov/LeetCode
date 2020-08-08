"""
    Serialization is the process of converting a data structure or object into 
    a sequence of bits so that it can be stored in a file or memory buffer, or 
    transmitted across a network connection link to be reconstructed later in 
    the same or another computer environment.
    Design an algorithm to serialize and deserialize a binary tree. There is no 
    restriction on how your serialization/deserialization algorithm should work. 
    You just need to ensure that a binary tree can be serialized to a string and 
    this string can be deserialized to the original tree structure.

    Example:
    You may serialize the following tree:
            1
           / \
          2   3
             / \
            4   5
    as "[1,2,3,null,null,4,5]"

    Clarification: The above format is the same as how LeetCode serializes 
                   a binary tree. You do not necessarily need to follow this 
                   format, so please be creative and come up with different 
                   approaches yourself.

    Note: Do not use class member/global/static variables to store states. 
          Your serialize and deserialize algorithms should be stateless.
"""
#Difficulty: Hard
#48 / 48 test cases passed.
#Runtime: 240 ms
#Memory Usage: 21.1 MB

#Runtime: 240 ms, faster than 14.61% of Python3 online submissions for Serialize and Deserialize Binary Tree.
#Memory Usage: 21.1 MB, less than 13.11% of Python3 online submissions for Serialize and Deserialize Binary Tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return
        queue = [root]
        serialize = []
        while queue:
            length = len(queue)
            level = []
            while length:
                length -= 1
                node = queue.pop(0)
                level.append(str(node.val) if node else 'null')
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
            for value in level[::-1]:
                if value != 'null':
                    serialize.extend(level)
                    break
        return ','.join(serialize)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = data.split(',')
        root = None
        index = 0
        count = len(data)
        return self.constructTree(root, data, count, index)

    def constructTree(self, root, data, count, index):
        """Tree construction function.

        :type root: None
        :type data: str
        :type count: int
        :type index: int
        :rtype: TreeNode
        """
        if index < count:
            root = TreeNode(data[index])
            left = 2 * index + 1
            right = 2 * index + 2
            root.left = self.constructTree(root.left, data, count, left)
            root.right = self.constructTree(root.right, data, count, right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

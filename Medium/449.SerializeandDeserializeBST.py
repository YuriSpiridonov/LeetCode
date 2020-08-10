"""
    Serialization is the process of converting a data structure or object into 
    a sequence of bits so that it can be stored in a file or memory buffer, or 
    transmitted across a network connection link to be reconstructed later in 
    the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary search tree. 
    There is no restriction on how your serialization/deserialization algorithm 
    should work. You just need to ensure that a binary search tree can be 
    serialized to a string and this string can be deserialized to the original 
    tree structure.

    The encoded string should be as compact as possible.

    Note: Do not use class member/global/static variables to store states. 
          Your serialize and deserialize algorithms should be stateless.
"""
#Difficulty: Medium
#62 / 62 test cases passed.
#Runtime: 168 ms
#Memory Usage: 20.8 MB

#Runtime: 168 ms, faster than 9.32% of Python3 online submissions for Serialize and Deserialize BST.
#Memory Usage: 20.8 MB, less than 5.02% of Python3 online submissions for Serialize and Deserialize BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return
        data = ""
        queue = [root]
        values = []
        while queue:
            current = queue.pop(0)
            if current:
                values.append(str(current.val))
            else:
                values.append('null')
            if current:
                queue.append(current.left)
                queue.append(current.right)
        length = len(values) - 1
        while values[length].isalpha():
            values.pop()
            length -= 1       
        return ','.join(values)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return
        data = data.split(',')
        i = 0
        count = len(data)
        root = None
        return self.constructTree(root, data, i, count)

    def constructTree(self, root, data, i, count):
        """Construct tree function.
        """
        if i < count:
            root = TreeNode(data[i])
            root.left = self.constructTree(root.left, data, 2 * i + 1, count)
            root.right = self.constructTree(root.right, data, 2 * i + 2, count)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

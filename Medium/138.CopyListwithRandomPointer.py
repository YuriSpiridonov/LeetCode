'''
    A linked list is given such that each node contains an 
    additional random pointer which could point to any node 
    in the list or null.

    Return a deep copy of the list.

    The Linked List is represented in the input/output as a 
    list of n nodes. Each node is represented as a pair of 
    [val, random_index] where:

        - val: an integer representing Node.val
        - random_index: the index of the node (range from 0 
          to n-1) where random pointer points to, or null 
          if it does not point to any node.

    Example:
    Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

    Example:
    Input: head = [[1,1],[2,1]]
    Output: [[1,1],[2,1]]

    Example:
    Input: head = [[3,null],[3,0],[3,null]]
    Output: [[3,null],[3,0],[3,null]]

    Example:
    Input: head = []
    Output: []
    Explanation: Given linked list is empty (null pointer), 
                 so return null.

    Constraints:
        - -10000 <= Node.val <= 10000
        - Node.random is null or pointing to a node in the 
          linked list.
        - The number of nodes will not exceed 1000.
'''
#Difficulty: Medium
#19 / 19 test cases passed.
#Runtime: 32 ms
#Memory Usage: 15 MB

#Runtime: 32 ms, faster than 87.10% of Python3 online submissions for Copy List with Random Pointer.
#Memory Usage: 15 MB, less than 66.26% of Python3 online submissions for Copy List with Random Pointer.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return 

        # Coping nodes
        node = head
        while node:
            nxt = node.next
            node.next = Node(node.val)
            node = node.next
            node.next = nxt
            node = node.next

        # Handling random
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        # Adding copies to queue
        i = 0
        node = head
        queue = []
        while node:
            if i % 2:
                queue.append(node)
            node = node.next
            i+=1

        # Reconstructing cloned Linked List
        clone = Node(0)
        node = clone 
        while queue:
            node.next = queue.pop(0)
            node = node.next

        return clone.next
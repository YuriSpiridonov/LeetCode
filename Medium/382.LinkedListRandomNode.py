"""
    Given a singly linked list, return a random node's value from the linked 
    list. Each node must have the same probability of being chosen.

    Follow up:
    What if the linked list is extremely large and its length is unknown to 
    you? Could you solve this efficiently without using extra space?

    Example:
            // Init a singly linked list [1,2,3].
            // ListNode head = new ListNode(1);
            // head.next = new ListNode(2);
            // head.next.next = new ListNode(3);
            // Solution solution = new Solution(head);

            // getRandom() should return either 1, 2, or 3 randomly. 
            // Each element should have equal probability of returning.
            // solution.getRandom();
"""
#Difficulty: Medium
#7 / 7 test cases passed.
#Runtime: 68 ms
#Memory Usage: 17.4 MB

#Runtime: 68 ms, faster than 94.68% of Python3 online submissions for Linked List Random Node.
#Memory Usage: 17.4 MB, less than 22.43% of Python3 online submissions for Linked List Random Node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, 
        so it contains at least one node.
        """
        self.vals = []
        while head:
            self.vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.vals)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

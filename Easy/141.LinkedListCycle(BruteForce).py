"""
    Given head, the head of a linked list, determine if the linked list has 
    a cycle in it.

    There is a cycle in a linked list if there is some node in the list that
    can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next 
    pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return 
    false.

    Example:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects 
                 to the 1st node (0-indexed).

    Example:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects 
                 to the 0th node.

    Example:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

    Constraints:
        - The number of the nodes in the list is in the range [0, 10**4].
        - -10**5 <= Node.val <= 10**5
        - pos is -1 or a valid index in the linked-list.

    Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
#Difficulty: Easy
#17 / 17 test cases passed.
#Runtime: 52 ms
#Memory Usage: 17.1 MB

#Runtime: 52 ms, faster than 42.88% of Python3 online submissions for Linked List Cycle.
#Memory Usage: 17.1 MB, less than 99.22% of Python3 online submissions for Linked List Cycle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        count = 0
        while head:
            count += 1
            head = head.next
            if count > 10000:
                return True
        return False

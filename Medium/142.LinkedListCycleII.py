"""
    Given a linked list, return the node where the cycle begins. If there is
    no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that 
    can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next 
    pointer is connected to. Note that pos is not passed as a parameter.

    Notice that you should not modify the linked list.

    Example:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to 
                 the second node.

    Example:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to 
                 the first node.

    Example:
    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

    Constraints:
        - The number of the nodes in the list is in the range [0, 10**4].
        - -10**5 <= Node.val <= 10**5
        - pos is -1 or a valid index in the linked-list.

    Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
#Difficulty: Medium
#16 / 16 test cases passed.
#Runtime: 48 ms
#Memory Usage: 17.4 MB

#Runtime: 48 ms, faster than 78.73% of Python3 online submissions for Linked List Cycle II.
#Memory Usage: 17.4 MB, less than 99.99% of Python3 online submissions for Linked List Cycle II.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        while head:
            if head not in s:
                s.add(head)
                head = head.next
            else:
                break
        return head

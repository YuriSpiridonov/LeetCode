"""
    Given the head of a linked list, we repeatedly delete consecutive sequences 
    of nodes that sum to 0 until there are no such sequences.
    After doing so, return the head of the final linked list.  You may return 
    any such answer.
    (Note that in the examples below, all sequences are serializations of 
    ListNode objects.)

    Example:
    Input: head = [1,2,-3,3,1]
    Output: [3,1]
    Note: The answer [1,2,1] would also be accepted.

    Example:
    Input: head = [1,2,3,-3,4]
    Output: [1,2,4]

    Example:
    Input: head = [1,2,3,-3,-2]
    Output: [1]

    Constraints:
        - The given linked list will contain between 1 and 1000 nodes.
        - Each node in the linked list has -1000 <= node.val <= 1000.
"""
#Difficulty: Medium
#105 / 105 test cases passed.
#Runtime: 5392 ms
#Memory Usage: 14.1 MB

#Runtime: 5392 ms, faster than 5.07% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
#Memory Usage: 14.1 MB, less than 48.68% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        stack = []
        while head:
            if head.val != 0:
                stack.append(head.val)
            head = head.next
        i = 0
        j = 0
        l = len(stack)
        while i < l:
            if sum(stack[i:j+1]) == 0:
                stack = stack[:i] + stack[j+1:]
                j = i
                l = len(stack)
            if j == l:
                j = i
                i += 1
            j += 1
        if not stack:
            return None
        node = ListNode(stack.pop(0))
        head = node
        while stack:
            node.next = ListNode(stack.pop(0))
            node = node.next
        return head

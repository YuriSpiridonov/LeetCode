"""
    Sort a linked list using insertion sort.

    Algorithm of Insertion Sort:
        1. Insertion sort iterates, consuming one input element each 
           repetition, and growing a sorted output list.
        2. At each iteration, insertion sort removes one element from the 
           input data, finds the location it belongs within the sorted list, 
           and inserts it there.
        3. It repeats until no input elements remain.

    Example:
    Input: 4->2->1->3
    Output: 1->2->3->4

    Example:
    Input: -1->5->3->4->0
    Output: -1->0->3->4->5
"""
#Difficulty: Medium
#22 / 22 test cases passed.
#Runtime: 68 ms
#Memory Usage: 16 MB

#Runtime: 68 ms, faster than 96.17% of Python3 online submissions for Insertion Sort List.
#Memory Usage: 16 MB, less than 13.80% of Python3 online submissions for Insertion Sort List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        queue = [head]
        node = head.next
        while node:
            if node.val < queue[-1].val:
                i = self.binarySearch(queue, node.val)
                queue.insert(i, node)
            else:
                queue.append(node)
            node = node.next
        head = queue.pop(0)
        node = head
        while queue:
            node.next = queue.pop(0)
            node = node.next
        node.next = None
        return head

    def binarySearch(self, array, target):
        left = 0
        right = len(array) - 1
        while left <= right:
            middle = (left+right) // 2
            if left == middle and target < array[middle].val:
                return middle
            elif target > array[middle].val:
                left = middle + 1
            else:
                right = middle - 1
        return middle + 1

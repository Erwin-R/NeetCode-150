"""
Problem:
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.

Test Cases: 
    Example 1:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
    Example 2:
        Input: list1 = [], list2 = []
        Output: []
    Example 3:
        Input: list1 = [], list2 = [0]
        Output: [0]
"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        current = newList

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else: 
                current.next = list2
                list2 = list2.next
            current = current.next

        #if there are leftover values in one of the lists
        current.next = list2 if not list1 else list1

        return newList.next
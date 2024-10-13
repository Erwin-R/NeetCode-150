"""
Problem: 
    Given the head of a singly linked list, reverse the list, and return the reversed list.

Test Cases: 
    Example 1:
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]
    Example 2:
        Input: head = [1,2]
        Output: [2,1]
    Example 3:
        Input: head = []
        Output: []
"""

#Time: O(n) where n is the size of the linked list 
#Space: O(1) 

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
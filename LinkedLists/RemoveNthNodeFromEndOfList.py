"""
Problem: 
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

Test Case: 
    Example 1:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]
    Example 2:
        Input: head = [1], n = 1
        Output: []
    Example 3:
        Input: head = [1,2], n = 1
        Output: [1]
"""

#Time: O(n) where n is the size of the linked list
#Space: O(1) not using extra space, just references to nodes

class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        slow = fast = dummy
        for i in range(n):
            fast = fast.next
        
        while fast.next: 
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next
    
    
        #                   s         f
        #dummy -> 1 -> 2 -> 3 -> 4 -> 5


#Time: O(n) where n is the size of the linked list
#Space: O(1) not using extra space, just references to nodes
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        left = dummy
        right = head

        #distance between L and R is equal to n
        while n > 0 and right:
            right = right.next
            n -= 1
        
        #Going until we reach end of list
        while right:
            left = left.next
            right = right.next 
        
        #delete
        left.next = left.next.next
        return dummy.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            # Move to the next node
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        # Return the resulting list (skipping the dummy node)
        return dummy.next
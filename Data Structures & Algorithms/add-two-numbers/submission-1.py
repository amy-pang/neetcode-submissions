# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        overflow = 0
        while l1 or l2 or overflow:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            digit_sum = v1 + v2 + overflow
            overflow = digit_sum // 10
            digit_sum = digit_sum % 10

            curr.next = ListNode(digit_sum, None)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
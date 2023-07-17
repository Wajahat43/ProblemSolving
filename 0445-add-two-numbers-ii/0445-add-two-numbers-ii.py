# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        smaller = None
        larger = None

        def getSize(l):
            current = l
            size = 0
            while current:
                size += 1
                current = current.next
            return size
        
        def add(first,second):
            carry = 0
            next = None
            if first.next:
                carry,next = add(first.next,second.next)
            
            current = ListNode((first.val+second.val + carry)%10, next)
            carry = (first.val + second.val + carry) // 10
            return carry, current
            
            
        def addSingle(first,second,carry,size):
            
            if size > 1:
                carry, second = addSingle(first.next,second,carry,size-1)

            res = (first.val+carry)%10
            carry = (first.val + carry)//10
            current = ListNode(res,second)
            return carry, current
            
                

            
        s1 = getSize(l1)
        s2 = getSize(l2)
        diff = 0

        if s1 > s2:
            smaller = l2
            larger = l1
            diff = s1 - s2
        else:
            smaller = l1
            larger = l2
            diff = s2 - s1
        
        largerHead = larger
        

        for i in range(diff):
            larger = larger.next
            
        
        carry, head = add(larger, smaller)
        if diff > 0:
            carry,head = addSingle(largerHead, head, carry, diff)
        if carry != 0:
            return ListNode(carry, head)
        return head


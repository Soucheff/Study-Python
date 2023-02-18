#https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    list = ListNode()
    pl = list
    dec = 0
    while True:
        if l1 == None and l2 == None and dec==0:
            break
        
        if l1 == None:
            v1 = 0
        else:
            v1 = l1.val
            l1 = l1.next
            

        if l2 == None:
            v2 = 0
        else:
            v2 = l2.val
            l2 = l2.next

        sum = v1+v2+dec

        if sum > 9:
            sum = sum - 10
            dec = 1
        else:
            dec=0

        pl.val = sum

        if(l1 != None or l2 != None or dec==1) :            
            pl.next = ListNode()
        pl = pl.next

    return list

l1 = ListNode(val=9)
l1.next = ListNode(val=9)


l2 = ListNode(val=9)
l2.next = ListNode(val=9)
l2.next.next = ListNode(val=9)

print(addTwoNumbers(l1,l2))


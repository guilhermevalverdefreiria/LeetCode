# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        list1 = []
        list2 = []
        while l1 is not None:
            list1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            list2.append(l2.val)
            l2 = l2.next

        list1.reverse()
        list2.reverse()

        n1 = int("".join(map(str, list1)))
        n2 = int("".join(map(str, list2)))

        s = n1 + n2

        slist = list(map(int, str(s)))
        slist.reverse()
        

        g = ListNode()
        g.val = slist[0]
        head = g

        
        for i in range(1,len(slist)):
            g1 = ListNode(slist[i])
            g.next = g1
            g = g1

        return head

        
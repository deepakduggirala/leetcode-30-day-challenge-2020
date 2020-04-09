# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    def middleNode(self, head):
        if head is None:
            return head
        a = [head]
        while a[-1].next is not None:
            a.append(a[-1].next)

        return a[len(a)//2]

def list_to_listnode(xs):
    prev = None
    head = None
    for x in xs:
        if prev is not None:
            t = ListNode(x)
            prev.next = t
            prev = t
        else:
            prev = ListNode(x)
            head = prev
    return head

inputs = [
    list_to_listnode([1,2,3,4,5]),
    list_to_listnode([1,2,3,4,5,6]),
    list_to_listnode(range(101))
]

for i in inputs:
  print(Solution().middleNode(i), '\n')
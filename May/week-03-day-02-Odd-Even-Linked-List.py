'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def oddEvenList(self, head):
    if head is None:
      return head
    if head.next is None:
      return head
    even_head = head.next
    even_tail = head.next
    odd_head = head
    odd_tail = head
    
    i = 3
    head = head.next.next
    while head is not None:
      if i%2 == 0:
        # print('even_tail', even_tail.val, 'next is', head.val)
        even_tail.next = head
        even_tail = head
      else:
        # print('odd_tail', odd_tail.val, 'next is', head.val)
        odd_tail.next = head
        odd_tail = head
      i = i + 1
      head = head.next
    even_tail.next = None
    odd_tail.next = even_head
    return odd_head

def array_to_linkedlist(nums):
  head = None
  tail = None
  for n in nums:
    h = ListNode(val=n)
    if head is None:
      head = h
      tail = h
    else:
      tail.next = h
      tail = h
  return head

def linkedlist_to_array(head):
  nums = []
  while head is not None:
    nums.append(head.val)
    head = head.next
  return nums

inputs = [
  range(5),
  range(6),
  [],
  [0],
  [1,2],
  [1,2,3]
]

for i in inputs:
  print(i, linkedlist_to_array(Solution().oddEvenList(array_to_linkedlist(i))))
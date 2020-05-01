'''
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
'''
class DLNode:
  def __init__(self, v):
    self.value = v
    self.prev = None
    self.next = None




class FirstUnique:
  def __init__(self, nums):
    self.head = None
    self.tail = None
    self.set = set()
    self.DLHash = {}
    for n in nums:
      self.add(n)

  def showFirstUnique(self):
    return self.head.value if self.head is not None else -1
        
  def add(self, value):
    if value in self.set: # no longer unique
      if value in self.DLHash:
        node = self.DLHash.pop(value)
        self.remove(node)
    else: #unique
      self.set.add(value)
      new_node = self.add_at_end(value)
      self.DLHash[value] = new_node

  def add_at_end(self, value):
    new_node = DLNode(value)
    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    return new_node
  
  def remove(self, node):
    if node.prev is None and node.next is None:
      self.head = None
      self.tail = None
    elif node.prev is None: #head
      n = node.next
      self.head = n
      n.prev = None
    elif node.next is None: #tail
      p = node.prev
      self.tail = p
      p.next = None
    else:
      p = node.prev
      n = node.next
      p.next = n
      n.prev = p
        
obj = FirstUnique([2,3,5])
print(obj.showFirstUnique())
obj.add(5)
print(obj.showFirstUnique())
obj.add(2)
print(obj.showFirstUnique())
obj.add(3)
print(obj.showFirstUnique())

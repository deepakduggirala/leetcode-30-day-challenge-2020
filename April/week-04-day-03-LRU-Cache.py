class DLNode:
  def __init__(self, k, v):
    self.key = k
    self.value = v
    self.prev = None
    self.next = None

class LRUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.hash = {}
    self.curr_capacity = 0
    self.dl_first = None
    self.dl_last = None

  def get(self, key):
    if key in self.hash:
      node = self.hash[key]
      self._updateNode(node)
      return node.value
    else:
      return -1

  def put(self, key, value):
    if key in self.hash:
      node = self.hash[key]
      node.value = value
      self._updateNode(node)
    else:
      if self.curr_capacity == self.capacity:
        self.hash.pop(self.dl_last.key)
        self._removeNode(self.dl_last)
        
      node = DLNode(key, value)
      self.hash[key] = node
      self._addNode(node)

  def _addNode(self, node):
    if self.curr_capacity != 0:
      node.next = self.dl_first
      node.prev = None
      self.dl_first.prev = node
      self.dl_first = node
    else:
      self.dl_first = node
      self.dl_last = node
      node.next = None
      node.prev = None
    self.curr_capacity = self.curr_capacity + 1

  def _removeNode(self, node):
    if node.next is None and node.prev is None: # only node
      self.dl_first = None
      self.dl_last = None
    elif node.next is None: #last node
      p = node.prev
      p.next = None
      self.dl_last = p
    elif node.prev is None: #first node
      n = node.next
      n.prev = None
      self.dl_first = n
    else: # middle node
      print('middle node')
      p = node.prev
      n = node.next
      p.next = n
      n.prev = p
    self.curr_capacity = self.curr_capacity - 1

  def _updateNode(self, node):
    self._removeNode(node)
    self._addNode(node)

def print_state(cache): 
  print(cache.hash) 
  node = cache.dl_first 
  s=[] 
  while True:
    if node is None:
      break
    s.append(str(node.value))
    if node.next is None:
      break
    node = node.next 
  print('<->'.join(s))

  node = cache.dl_last
  s=[] 
  while True:
    if node is None:
      break
    s.append(str(node.value))
    if node.prev is None:
      break
    node = node.prev 
  print('<->'.join(s))

  print(cache.curr_capacity)

cache = LRUCache(3)

# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))       # returns 1
# cache.put(3, 3)    # evicts key 2
# print(cache.get(2))       # returns -1 (not found)
# cache.put(4, 4)    # evicts key 1
# print(cache.get(1))       # returns -1 (not found)
# print(cache.get(3))       # returns 3
# print(cache.get(4))       # returns 4

cache.put(2,1)
cache.put(2,2)
cache.put(1,1)
cache.put(3,3)
print_state(cache)

# exec(open('week-04-day-03-LRU-Cache.py').read()) 
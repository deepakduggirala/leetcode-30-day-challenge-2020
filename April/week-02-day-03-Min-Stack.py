'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   # Returns -3.
minStack.pop();
minStack.top();      # Returns 0.
minStack.getMin();   # Returns -2.
'''

class MinStack:
  
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            curr_min = self.stack[-1][1]
            if x < curr_min:
                minimum = x
            else:
                minimum = curr_min
            self.stack.append((x, minimum))
            

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
        else:
            return None

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        if len(self.stack) != 0:
            return self.stack[-1][1]
        else:
            return None

# class MinHeap:
#     def __init__(self):
#         self.heap = [0]

#     def insert(self, x):

minStack = MinStack();
print(minStack.top()); 
print(minStack.pop());
print(minStack.getMin());
print(minStack.push(-2));
print(minStack.push(0));
print(minStack.push(-3));
print(minStack.getMin());   # Returns -3.
print(minStack.pop());
print(minStack.top());      # Returns 0.
print(minStack.getMin());   # Returns -2.
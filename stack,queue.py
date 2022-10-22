# A queue follows FIFO rule (First In First Out) and used in programming for sorting.
'''A Stack is a data structure that follows the LIFO(Last In First Out) principle. To implement a stack, 
we need two simple operations:
push - It adds an element to the top of the stack.
pop - It removes an element from the top of the stack.'''

#Operations:
'''Adding - It adds the items in the stack and increases the stack size. The addition takes place at the top of the stack.
Deletion - It consists of two conditions, first, if no element is present in the stack, then underflow occurs in the stack, and second, if a stack contains some elements, then the topmost element gets removed. It reduces the stack size.
Traversing - It involves visiting each element of the stack.'''

#Queue
'''A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front.
To implement a queue, we need two simple operations:
enqueue - It adds an element to the end of the queue.
dequeue - It removes the element from the beginning of the queue.'''

#Operations on Queue
'''Addition - It adds the element in a queue and takes place at the rear end, i.e., at the back of the queue.
Deletion - It consists of two conditions - If no element is present in the queue, Underflow occurs in the queue, or if a stack contains some elements then element present at the front gets deleted.
Traversing - It involves to visit each element of the queue.'''

import queue   # Queue is created as an object 'L'  
L = queue.Queue(maxsize=10)   
  
# Data is inserted in 'L' at the end using put()   
L.put(9)   
L.put(6)   
L.put(7)   
L.put(4)   
# get() takes data from from the head of the Queue   
print(L.get())   
print(L.get())   
print(L.get())   
print(L.get())   
'''ARRAYS - are an ordered collection of elements with every value being of the same data type.
That is the most important thing to remember about Python arrays - 
the fact that they can only hold a sequence of multiple items that are of the same type'''
#Arrays are not a built-in data structure, and therefore need to be imported via the array module in order to be used.
#from array import *

#The general syntax for creating an array looks like this:
#variable_name = array(typecode,[elements])

'''variable_name would be the name of the array.
The typecode specifies what kind of elements would be stored in the array. 
Whether it would be an array of integers, an array of floats or an array of any other Python data type. Remember that all elements should be of the same data type.
Inside square brackets you mention the elements that would be stored in the array, with each element being separated by a comma. You can also create an empty array by just writing variable_name = array(typecode) alone, without any elements.'''

from array import*
from tkinter import N
number=array('i',[10,20,30])
print(number)
print(len(number))
print(number[2]) #Array indexing
print(number[-2]) #negative indexing 

for number in number: #for loop
    print(number)

number=array('i',[10,20,30])
print(number[:2]) #array slicing
print(number[1:3])

number[0]=40 #changing values in an array
print(number)

number.append(50) #adding a number in an array
print(number)

number.extend([60,70,80]) #extends the array with the added numbers
print(number)

 #Use the insert() method, to add an item at a specific position.
 #The insert() function takes two arguments: the index number of the position the new element will be inserted,
 # and the value of the new element.
number=array('i',[10,20,30]) 
number.insert(0,40)
print(number)

number=array('i',[10,20,30]) #removes the specified element from the array, incase of identical values the first value on the list will be removed
number.remove(20)
print(number)

#You can also use pop() to specify the position of the element to be remove
number=array('i',[10,20,30]) 
number.pop(0)
print(number)




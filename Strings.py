txt = ' I love Jesus '
print(txt.upper()) #  method returns the string in upper case:
print(txt.lower()) # method returns the string in lower case:
print(txt.strip()) # method removes any whitespace from the beginning or the end
print(txt.replace('l','L')) # method replaces a string with another string:
print(txt.split('love')) # method splits the string into substrings if it finds instances of the separator

'''String Concatenation
To concatenate, or combine, two strings you can use the + operator.'''
#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format
'''As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:'''
age = 36
txt = "My name is John, I am " + age
print(txt)
#But we can combine strings and numbers by using the format() method!
'''The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:'''

#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#or you can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

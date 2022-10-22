#A python module is simply a python file with .pyextensiion including statements and definitions
'''It contains codes that you can reuse in several programs''' #demo.py is a module with module name demo
#Types of python modules:
'''1) Built-in modules - predefined modules that are part of the python standard library e.g random, datetime, sys
2) User-defined modules - created but the user to ease complex tasks in projects'''

#in [1]

y=6
def add(a,b):
    results=a+b
    return results

#in [2]:
def multi(a,b):
    return a*b;
def divide(a,b):
    return a/b;

 #in [3]:
def remainder(a,b):
    return a%b;
def add10(a,b):
    result1=a+10
    result2=b+10
    return(result1,result2)

# In [3]
#Check for prime number - is always >1
def prime (n):
    if n>1:
        for i in range (2,n):
            if(n%i)==0:
                print(n, 'is not a prime number')
                break
            else:
                print(n,'is a prime number')
    else:
        print(n, 'is not a prime nummber')

# In [4]: the sorted stings are checked
def checkanagram(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print('The strings are anagrams')
    else:
        print("The strings aren't anagrams")    



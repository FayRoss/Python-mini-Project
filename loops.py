from email.contentmanager import raw_data_manager
from itertools import count
from msilib import RadioButtonGroup
from string import printable
from tabnanny import check


for number in range(3):
    print('Attempt',number+1, (number+1)*".")
    

successful=False
for number in range(3):
    print('Attempt')
    if successful:
        print("Successful")
        break
else:
    print('Attempted 3 times and failed')    
 

for number in range(3):
    print("Well done",number+1)

for x in range(5):
    for y in range(3):
        print(f"{x},{y}")


print(type(5))
print(type(range(5)))

for x in 'Python':
    print(x)
for x in[1,2,3,4]:
    print(x)

count=0
for x in range(1,15):
    if x%2==0:
        count+=1
        print(x)
print(f"{count} prime numbers ")


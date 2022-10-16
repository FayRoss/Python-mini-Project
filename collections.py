#LISTS - Square braces. Can comprise of diffferent datatypes
List1=['computer','Printer','Tv','camera']
print(List1)
List1[0]="PC"
print(List1)
print(List1)

#TUPPLE - Rounded braces. A tupple is immutable i.e you cannot change it once you create it
tupple1=('computer','Printer','Tv','camera') 
print(tupple1)

#SET - is a collection of a list enclosed in a round bracket and it uses the set keyword i.e set1=set(keyword)([])
#The output is in curly brackets i.e {output}
set1= set(['computer','Printer','Tv','camera']) 
print(set1)

#DICTIONARY - Curly braces. The key cannot be changes but can change the values.
dict1={1:'Monday',2:'Tuesday',3:'Wednesday'}
print(dict1)

dict2={
    1:'Mathematics',
    2:'English',
    3: 'Science'
}

#[LISTS],(TUPPLES),([SET]) and DICTIONARY can all take in different datatypes at the same time i.e int, str etc.

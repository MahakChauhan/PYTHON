#Sets are unordered collection of data items.Sets are unchangeable. Sets do not contain duplicate values.
s={11,2,31,4,3}
print(s)
info={"carlo",True,10,10,34}
print(info)
#Creation of empty set
S1=set()
print(type(S1))
#Accesssing the elements of set
for i in s:
    print(i)
"""
Output=
{2, 3, 4, 11, 31}
{True, 10, 34, 'carlo'}
<class 'set'>
2
3
4
11
31
"""
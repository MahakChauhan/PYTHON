marks=[2,3,4,5,"Mahak",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
# print(marks[6]) #index out of bound
print(marks[-2]) #negative index
print(marks[len(marks)-2]) #positive index
print(marks[6-2]) #positive index
print(marks[4]) #positive index
#Check whether an item is present in the list
if 3 in marks:
    print("Yes")
else:
    print("No")
#Same thing applies for string as well    
if "aha" in "mahak":
    print("yes")
else:
    print("No")
print(marks)
print(marks[:])
print(marks[1:4])
print(marks[1:8:2])
#list comprehension
list =[i for i in range(10)]
print(list)
list =[i*i for i in range(10) if i%2==0]
print(list)
"""
Output=
[2, 3, 4, 5, 'Mahak', True]
<class 'list'>
2
3
4
5
Mahak
True
Mahak
Mahak
Mahak
Mahak
Yes
yes
[2, 3, 4, 5, 'Mahak', True]
[2, 3, 4, 5, 'Mahak', True]
[3, 4, 5]
[3, 5, True]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 4, 16, 36, 64]
"""
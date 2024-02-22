tup=(20,43,9,81,1,4,"mhk")
print(type(tup),tup)
# tup[0]=23 #throws an error
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
# print(marks[6]) #index out of bound
print(tup[-2]) #negative index
print(tup[len(tup)-2]) #positive index
print(tup[6-2]) #positive index
print(tup[4]) #positive index
#Check whether an item is present in the list
if 43 in tup:
    print("Yes 43 is present in the tuple")
else:
    print("No")
#Same thing applies for string as well    
if "h" in "mhk":
    print("yes")
else:
    print("No")
print(tup)
print(tup[:])
print(tup[1:4])
print(tup[1:8:2])
#list comprehension
list =[i for i in range(10)]
print(list)
list =[i*i for i in range(10) if i%2==0]
print(list)
"""
Output=
7
20
43
9
81
1
4
4
4
1
1
Yes 43 is present in the tuple
yes
(20, 43, 9, 81, 1, 4, 'mhk')
(20, 43, 9, 81, 1, 4, 'mhk')
(43, 9, 81)
(43, 81, 4)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 4, 16, 36, 64]
"""
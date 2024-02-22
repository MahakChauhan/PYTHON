#Tuples are immutable
tup1=(2,45,1,9,34,10,45)
print(tup1)
# temp=list(tup1)
# temp.append("Mahak")
# temp.append(True)
# temp[1]=19
# tup1=tuple(temp)
print(tup1)
tup3=(1,2,4,5,6)
tup4=(34,67)
temp=tup3+tup4
print(temp)
res=tup1.count(45)
print("Number of occurence of particular item in the tuple are: ",res)
res=tup1.index(45)
print("Index number is : ",res)
res=tup1.index(9,2,6)
print("Index number is : ",res)
"""
Output=
(2, 45, 1, 9, 34, 10, 45)
(2, 45, 1, 9, 34, 10, 45)
(1, 2, 4, 5, 6, 34, 67)
Number of occurence of particular item in the tuple are:  2
Index number is :  1
Index number is :  3
"""
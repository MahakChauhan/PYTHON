#lists are changeable
l=[9,12,4,1,7,7,30]
print(l)
l.append(13)
print(l)
l.sort() #ascending order
print(l)
# l.sort(reverse=True) #descending order
# print(l)
l.reverse()
print(l)
print(l.index(9)) #return index of the given item
print(l.count(7))
m=l.copy()
m[0]=101
print(l)
l.insert(1,37) #insert 37 at index 1
print(l)
m=[10,20,30]
k=l+m
l.extend(m)
print(l)
print(k)
"""
Output=
[9, 12, 4, 1, 7, 7, 30]
[9, 12, 4, 1, 7, 7, 30, 13]
[1, 4, 7, 7, 9, 12, 13, 30]
[30, 13, 12, 9, 7, 7, 4, 1]
3
2
[30, 13, 12, 9, 7, 7, 4, 1]
[30, 37, 13, 12, 9, 7, 7, 4, 1]
[30, 37, 13, 12, 9, 7, 7, 4, 1, 10, 20, 30]
[30, 37, 13, 12, 9, 7, 7, 4, 1, 10, 20, 30]
"""
s={1,4,2,6}
s1={3,1,2,5}
print(s.union(s1))
s.update(s1) #it will update s set and include s1 element also in the s set
print(s,s1)
a=s.intersection(s1)
print(a)
s.intersection_update(s1)
print(s)
a=s.symmetric_difference(s1) #it will show  those element which is not common to both of them
print(a)
a=s.difference(s1) #it will show  those element which is not common to both of them
print(a)
print(s.isdisjoint(s1)) #return boolean value either both sets are disjoint or not
print(s.issuperset(s1))
s1={1,2,3,4}
s2={2}
print(s2.issubset(s1))
s1.add(10)
print(s1)
s1.remove(2)
s1.discard(10)
print(s1)
item=s1.pop()
print(item)
if 2 in s1:
    print("yes")
else:
    print("no")   
s1.clear();
print(s1)
# del s1
"""
Output=
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6} {1, 2, 3, 5}
{1, 2}
{1, 2}
{3, 4, 5, 6}
{4, 6}
False
False
True
{1, 2, 3, 4, 10}
{1, 3, 4, 10}
{1, 3, 4}
1
no
set()
"""

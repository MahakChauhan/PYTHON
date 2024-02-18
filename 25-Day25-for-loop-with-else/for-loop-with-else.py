for i in range(3):
    print(i)
    
else:
    print("No more i")  
print("\n")
for i in range(6):
    print(i)
    if i==4:
        break  # else will not execute after this if statement
else:
    print("No more i")    
print("\n")
i=1
while i<6:
    print(i)
    i=i+1
    if i==5:
     break
else:
    print("no more i")
"""
Output=
0
1
2
No more i


0
1
2
3
4


1
2
3
4
"""
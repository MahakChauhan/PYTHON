for i in range(1,12):
    if(i==10):
     break # break statement enables a program to skip over a part of the code
    print("5*",i,"=",5*i)
for i in range(1,12):
    if(i==10):
     print("Skip the iteration")
     continue #continue statement skip the iteration
    print("5*",i,"=",5*i)
"""
Output=
5* 1 = 5
5* 2 = 10
5* 3 = 15
5* 4 = 20
5* 5 = 25
5* 6 = 30
5* 7 = 35
5* 8 = 40
5* 9 = 45
5* 1 = 5
5* 2 = 10
5* 3 = 15
5* 4 = 20
5* 5 = 25
5* 6 = 30
5* 7 = 35
5* 8 = 40
5* 9 = 45
Skip the iteration
5* 11 = 55
"""    
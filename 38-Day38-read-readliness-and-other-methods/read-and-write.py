f=open("myfile.txt",'r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line :
     break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of student {i} in Maths  is {m1}")
    print(f"Marks of student {i}  in SSt is {m2}")
    print(f"Marks of student {i} is Arts {m3}")

"""
Output=
Marks of student 1 in Maths  is 24
Marks of student 1  in SSt is 41
Marks of student 1 is Arts 45

Marks of student 2 in Maths  is 89
Marks of student 2  in SSt is 45
Marks of student 2 is Arts 90

Marks of student 3 in Maths  is 34
Marks of student 3  in SSt is 87
Marks of student 3 is Arts 90
"""
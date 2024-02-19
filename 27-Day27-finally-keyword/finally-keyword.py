def func():
    try:
        list=[10,20,35,45]
        i=int(input("Enter  a index="))
        print(list[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always executed")
x=func()
print(x)    
"""
If we enter  number in a index then=
Enter  a index=2
35
I am always executed
1....
If we enter  number out of index then=
Enter  a index=5
some error occured
I am always executed
0
"""  



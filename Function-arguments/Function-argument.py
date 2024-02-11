def average(a=9,b=6): #default argument
    print("The average is : ",(a+b)/2)
average(a=6) #it will take the value of a=6 and b default value will be 6
average(b=22,a=6) #order is not matter in keyword argument
def sum(a,b=6): #Here a is a required argument ,We have to provide the value of a while calling the function
    print("The sum is : ",a+b)
# sum(b=3) #it will give error while value of a is must to provide
sum(2)
#variable length argument
def Average(*numbers): #take n numbers of argument while calling
    sum=0
    for i in numbers:
     sum=sum+i
    print("The Average of numbers is ",sum/len(numbers))
Average(10,20,30)
def average(a=9,b=6): #default argument
    return (a+b)/2
c=average(2,30)
print(c)
"""
Output=
The average is :  6.0
The average is :  14.0
The sum is :  8
The Average of numbers is  20.0
16.0
"""
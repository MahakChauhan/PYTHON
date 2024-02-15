#factorial(5)=5*4*3*2*1
#factorial of a number
def factorial(num):
    if(num==0 or num==1):
        return 1;
    else:
        return num*factorial(num-1)
print(factorial(5))
# num*factorial(num-1)
# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*2*factorial(1)
# 5*4*3*2*1



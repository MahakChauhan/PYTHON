x=10
def fun():
    global x
    x=11
    print(f"The value of local x is {x}")
    y=20

fun()
print(f"The value of global x is {x}")
print(x)
print(y)
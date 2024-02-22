a=int(input("Enter a number="))
# a is the variable to match
match a:
 case 0:
  print("a is zero")
 case 4:
  print("Case is 4")
 
#case with if condition 
 case _ if a!=10:
  print("a is not equal to 10")
 case _ if a!=20:
  print("a is not equal to 20")
 case _:
  print(a)
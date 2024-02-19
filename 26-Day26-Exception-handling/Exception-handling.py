a=input("Enter a number=")
print(f"Multiplication of {a} is: ")
try:
  for i in range(1,11):
    print(f"{int(a)}X{i}={int(a)*i}")
except Exception as e:
  print("Entered number is not an integer")
print("End of program")
try:
  num=int(input("Enter a number="))
  a=[12,34,34]
  print(a[num])
except ValueError:
 print("Enter a integer")
except IndexError:
  print("Out of index")
  
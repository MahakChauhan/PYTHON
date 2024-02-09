a=int(input("Enter your age="))
#if-else conditional statement
if(a<18):
    print("You can not drive")
else:
    print("You can drive")   
#if-else elif 
num=int(input("Enter a number="))
if(num<0):
  print("Number is negative")
elif(num==0):
 print("Number is zero") 
else:
   print("Number is positive")
# nested if-else elif 
num=int(input("Enter a number="))
if(num<0):
  print("Number is negative")
elif(num>0):
 if(num>10 and num<20):
  print("Number is between  10-20")
 elif(num>20 and num<30):
  print("Number is between 20-30")
 else: 
  print("Out of range")  
else:
   print("Number is zero")    
    

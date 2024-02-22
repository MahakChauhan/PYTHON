"""In python, anything that you enclose between single or double quotation marks is considered a string.
 A string is essentially a sequence or array of textual data. """
#Example=
name="Mahak"
print(name)
print("My name is",name)
#Multiline string
a="""my name is Mahak 
I am a bca student.
I want to eat an apple"""
print(a)
#Accessing Characters of a String
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
a="Mahak Chauhan"
a1="!!Mahak!!"
m="aditya"
# print(name[5]) throws an error because 5 is out of index in String name
#print character using for loops
for character in name:
 print(character)
#Strings method
print(len(name)) #len() function is used to find a length of a string.
print(name.upper()) #The upper() method converts a string to upper case.
print(name.lower()) #The lower() method converts a string to lower case.
print(a.strip()) #The strip() method removes any white spaces before and after the string.
print(a1.rstrip("!")) #the rstrip() removes any trailing characters.
print(name.replace('k','l')) #The replace() method replaces all occurences of a string with another string. 
print(a.split()) 
print(m.capitalize()) #The capitalize() method turns only the first character of the string to uppercase
print(a.center(50)) #The center() method aligns the string to the center as per the parameters given by the user.
print(name.count(a)) #The center() method aligns the string to the center as per the parameters given by the user.
print(name.endswith('k'))
str1 = "He is s name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.index("Dan")) #returns index of given character
str2="WelcomeToTheWorld"
print(str2.isalnum()) 
"""The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. 
If any other characters or punctuations are present, then it returns False."""
print(name.isalpha())
str1 = "hello world"
print(str1.islower())
#The islower() method returns True if all the characters in the string are lower case, else it returns False.
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
#The isprintable() method returns True if all the values within the given string are printable,
str1 = "         "       #using Spacebar
print(str1.isspace())
#The isspace() method returns True only and only if the string contains white spaces, else returns False.
str1 = "World Health Organization" 
print(str1.istitle())
str2 = "To kill a Mocking bird"
print(str2.istitle())
"""The istitile() returns True only if the first letter of each word of the string is capitalized,
 else it returns False."""
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
"""The swapcase() method changes the character casing of the string. 
Upper case are converted to lower case and lower case to upper case."""
str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) #The title() method capitalizes each letter of the word within the string.
"""
OUTPUT-
Mahak
My name is Mahak
my name is Mahak
I am a bca student.
I want to eat an apple
M
a
h
a
k
M
a
h
a
k
5
MAHAK
mahak
Mahak Chauhan
!!Mahak
Mahal
['Mahak', 'Chauhan']
Aditya
                  Mahak Chauhan
0
True
3
16
True
True
True
False
True
True
False
True
pYTHON IS A iNTERPRETED lANGUAGE
His Name Is Dan. Dan Is An Honest Man.
"""
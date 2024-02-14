# String Formatting
letter="My name is {0} and I am from {1}"
name="Mahak"
country="India"
print(letter.format(name,country))
#f-strings
print(f"My name is {name} and I am from {country}")
print(f"My name is {{name}} and I am from {{country}}")
price=49.0996
txt=f"For only {price:.2f} dollars!"
print(txt.format())
print(type(f"{2*30}"))
"""
Output=
My name is Mahak and I am from India
My name is Mahak and I am from India
My name is {name} and I am from {country}
For only 49.10 dollars!
<class 'str'>
"""
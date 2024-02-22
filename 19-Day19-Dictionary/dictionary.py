dic={"Mahak":"Human being","Chair":"object"}
print(dic["Mahak"])
dict={1:"Mhk",2:"Eshika",3:"Ashwina",4:"Arti"}
print(dict[2])
print(type(dict))
print(dict[1]) #it will give error if value is not exist
print(dict.get(14)) #return  value if exist either return none
print(dict.keys())
print(dict.values())
print(dict.items()) #it will give key value pairs
# #accessing multiple keys
for key,value in dict.items():
    print(f"The value of corresponding {key} is {value}")
"""
Output=
Human being
Eshika
<class 'dict'>
Mhk
None
dict_keys([1, 2, 3, 4])
dict_values(['Mhk', 'Eshika', 'Ashwina', 'Arti'])
dict_items([(1, 'Mhk'), (2, 'Eshika'), (3, 'Ashwina'), (4, 'Arti')])
The value of corresponding 1 is Mhk
The value of corresponding 2 is Eshika
The value of corresponding 3 is Ashwina
The value of corresponding 4 is Arti
"""
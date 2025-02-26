## PYTHON DATA TYPES & SPECIAL KEYWORDS:

#string data type
id_card = """Name : Ummey Habiba
F/Name : Syed Amanullah
Age : 23"""
print(type(id_card))
print(id_card)

#integer data type
num = 35
print(type(num))
print(num)

#float data type
float_num = 1.3
print(type(float_num))
print(float_num)

#Boolean data type
is_true = True
is_false = False
print(type(is_true))
print(is_true)

#list data type
list_card = ["onion","potatoes","tomatoes","brinjal"]
print(type(list_card))
print(list_card)

#tuple data type
tuple_data = ("one","two","three")
print(type(tuple_data))
print(tuple_data)

#dictionary data type
dict_book = {"name": "habiba",
             "age" : "23"}
print(type(dict_book))
print(dict_book)

#set data type
fruits = {"apple","orange"}
print(type(fruits))
print(fruits)

#none data type
value = None
if value is None:
    print("value contains no value")
    print(type(value))

#from dictionary
frozen_clothes = frozenset(["frok","jacket","golves"])
print(frozen_clothes)
print(type(frozen_clothes))

# Example using Python special keywords

# True and False (Boolean values)
is_python_fun = True
print(is_python_fun)  # Output: True

# None (Represents the absence of a value)
value = None
print(value)  # Output: None

# if, elif, else (Conditional statements)
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

# for and while (Loops)
for i in range(3):
    print("Loop iteration {i}")

count = 0
while count < 3:
    print("While loop iteration {count}")
    count += 1

# def (Function definition)
def greet(name):
    return "Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# import (Importing modules)
import math
print(math.sqrt(16))  # Output: 4.0

# try, except (Exception handling)
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")

# class (Defining a class)
class Animal:
    def sound(self):
        return "Some sound"

dog = Animal()
print(dog.sound())  # Output: Some sound

# lambda (Anonymous function)
square = lambda x: x * x
print(square(4))  # Output: 16
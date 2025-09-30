"""
#PRINT OPERATIONS
- Can do both string, integer, float, and boolean operations

#INTEGER OPERATIONS
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Modulus (%)
- Exponentiation (**)
- Floor Division (//)

#FLOAT OPERATIONS
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Modulus (%)
- Exponentiation (**)
- Floor Division (//)

#STRING OPERATIONS
- Concatenation (+)
- Repetition (*)

#BOOLEAN OPERATIONS
- AND (and)
- OR (or)
- NOT (not)

#COMPARISON OPERATORS
- Equal to (==)
- Not equal to (!=)
- Greater than (>)
- Less than (<)
- Greater than or equal to (>=)
- Less than or equal to (<=)

#STRING METHODS
- upper() - Converts all characters in a string to uppercase.
- lower() - Converts all characters in a string to lowercase.
- strip() - Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove).
- replace(old, new) - Replaces all occurrences of a substring with another substring.
- split(separator) - Splits a string into a list where each word is a list item.
- find(substring) - Searches the string for a specified substring and returns the position of where it was found.
- join(iterable) - Joins the elements of an iterable (e.g., list, tuple) to the end of the string.
- format() - Formats specified values in a string.
- index() - Returns the index of the first occurrence of a substring in the string.

#TYPE CASTING
- str() - Converts a value to a string.
- int() - Converts a value to an integer.
- float() - Converts a value to a float.
- bool() - Converts a value to a boolean.
"""
x = 10
y = 3
z = x + y
print("Integer Operations")
print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor Division

x = 10.0
y = 3.0
print("Float Operations")
print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor Division

x = "Hello"
y = "World"
print("String Operations")
print(x + " " + y) # Concatenation
print(x * 3) # Repetition

x = True
y = False
print("Boolean Operations")
print(x and y) # AND
print(x or y) # OR
print(not x) # NOT

x = 10
y = 3
print("Comparison Operators")
print(x == y) # Equal to
print(x != y) # Not equal to
print(x > y) # Greater than
print(x < y) # Less than
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to

x = " Hello World World"
y = ["Hello", "World", "Python"]
print("String Methods")
print(x.upper()) # Converts all characters in a string to uppercase.
print(x.lower()) # Converts all characters in a string to lowercase.
print(x.strip()) # Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove).
print(x.replace("World", "Everyone")) # Replaces all occurrences of a substring with another substring.
print(x.split(" ")) # Splits a string into a list where each word is a list item.
print(x.find("World")) # Searches the string for a specified substring and returns the position of where it was found.
print(" ".join(x.split(" "))) # Joins the elements of an iterable (e.g., list, tuple) to the end of the string.
print("My name is {}, i am {} years".format("John", 23)) # Formats specified values in a string.
print(len(x)) # Returns the length of the string
print(x.count("World")) # Returns the number of occurrences of a substring in the string
print("123".isdigit())
name = "John"
age = 23
print(f"My name is {name} and I am {age}") # f-string for formatting strings

esaay = '''Hi my name sis ongdn
fjovnf
jsgsfn
bsfbs
fs
'''
print(esaay)
#String indexing and slicing
print(x[1]) # Second character
print(x[1:30]) # Characters from position 1 to 4

test = "Hello John, welcome to class John nice to meet you John"
# print(test.replace("John", "Jane",)) # Replaces first 2 occurrences of "John" with "Jane"

print("replacing John with Jane using a for loop")
print(test)
test_list = test.split()
for i in test_list:
    if i == "John":
        John_index = test_list.index(i)
        test_list[John_index] = "Jane"

print(test_list)
print(" ".join(test_list))
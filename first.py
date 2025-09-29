"""
Python Rules

1: Python Uses indentation to define code blocks
2: Python is case sensitive
3: Python doesn't allow default keywords as variable names
4: Python reads code from top to bottom
"""

###VARIABLES - things that store data in python
"""
Format 

variable_name assignment_operator value
Example:

first_name = "John"

#Rules for naming variables
1: Variable names should not be too long or too short
2: Variable names should not start with a number
3: Variable names should not contain special characters except for _ (underscore)
4: Variable names should not be the same as python keywords
5: Variable names must start with a letter or an underscore
"""

print("Hello World!")

first_name = "John"
last_name = "Doe"
fn = "Jane"  # short variable name
the_name_of_the_university_i_attend = "Harvard"  # long variable name
university_name = "MIT"  # good variable name

First_name = "John"
firstName = "John"
first_name = "John"  # preferred variable name style in python
print("Hello " + first_name + " " + last_name)


"""
DATA TYPES IN PYTHON

1: String - str - a sequence of characters enclosed in single or double quotes
example: "Hello", 'John', "123"
str(34) -> "34"

2: Integer - int - whole numbers without a decimal point
example: 1, 2, 3, -4, 0
int("34") -> 34

Float - float - numbers with a decimal point
example: 1.5, 2.0, -3.4, 0.0
float("3.4") -> 3.4

Boolean - bool - represents two values: True or False

"""
x = "1"
y = '3'
z = str("4")  # converting integer to string
print(type(4))
print(x + y + z)  # concatenation

zz = int(z)
print(type(zz))
print(zz + 3)  # addition

yy = float(y)
xx = float(x)

print(xx + yy)
print(int(4 / 2))
print(4 * 2.0)

is_raining = False
is_sunny = False

x = 2343
y = 87865
z = 1234

print(x < 5000)
if x > 5000:
    print("X is a High Salary earner")
else:
    print('X is not a high salary earner')


if y > 5000:
    print("Y is a High Salary earner")
else:
    print('Y is not a high salary earner')


if z > 5000:
    print("Z is a High Salary earner")
else:
    print('Z is not a high salary earner')


count = 0
running = True

while running:
    print(count)
    count += 1
    # if count > 10:
    #     running = False
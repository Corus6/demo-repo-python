"""
CONTROL FLOW

CONDITIONAL STATEMENTS
structure:
if condition: (run block of code)
elif condition: (run block of code)
else: (run block of code)

IF
ELIF
ELSE

Nesting - putting one control flow inside another control flow

LOOPS - for, while
FOR - loop through a sequence (list, tuple, string) or other iterable objects
WHILE - loop through a block of code as long as the condition is true

break - exit the loop
continue - skip the current iteration and move to the next iteration
pass - does nothing, acts as a placeholder
"""

x = 10
y = -5
z = 0
condition = x > 0 or y > 0 or z > 0
if x > 0:
    print("X is a positive number")
    if y < 0:
        print("Y is a positive number")
        if z == 0:
            print("Z is zero")
            if True:
                print("This will always execute")
            else:
                print("This will never execute")
        else:
            print("Z is a negative number")
    else:
        print("Y is a negative number")



# if x > 0:
#     print("X is a negative number")
#
# if x > 0:
#     print("X is zero")
elif x > 0:
    print("X is zero")
    if y < 0:
        print("Y is a positive number")
        if z == 0:
            print("Z is zero")
            if True:
                print("This will always execute")
            else:
                print("This will never execute")
        else:
            print("Z is a negative number")
    else:
        print("Y is a negative number")

else:
    print("X is a negative number or zero")
    if y < 0:
        print("Y is a positive number")
        if z == 0:
            print("Z is zero")
            if True:
                print("This will always execute")
            else:
                print("This will never execute")
        else:
            print("Z is a negative number")
    else:
        print("Y is a negative number")

print("This will always execute")

#Grading System
# score = int(input("Enter your score: ")) #The input() function always returns a string, so we need to convert it to an integer using int()
#
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# elif score >= 50:
#     print("E")
# else:
#     print("F")

#Login System
# username = input("Enter your username: ")
# password = str(input("Enter your password: ")).strip().capitalize().lower() #Nested Constructions
#
# if username == "admin" and password == "password123":
#     print("Login successful")
# elif password == "helloworld":
#     print(f"Hi {username}, welcome back!")
# else:
#     print("Login failed")
#

#FOR LOOP

balance = 1000

for i in range(0, 11, 3): #0, 1, 2, 3, 4
    balance = balance + 100
    # balance += 100

print(f"final balance: {balance}")

my_fruits = ["apple", "banana", "cherry", "date"]
for fruit in my_fruits:
    print(fruit)

#WHILE LOOP
count = 0

while count < 20:
    count += 1
    print("Hey I'm still running: ", count)
    if count == 10:
        for i in range(0, -3, -1):
            print("Inner loop: ", i)
            break
        break
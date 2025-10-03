"""
Break
Continue
Pass
"""

# for i in range(10):
#     if i == 5:
#         print("Breaking the loop at i =", i)
#         break  # exit the loop
#     print(i)
#
# for i in range(10):
#     if i == 5:
#         print("Continue the loop without i =", i)
#         continue  # skip this
#     print(i)
#
# for i in range(10):
#     if i == 5:
#         pass  # does nothing
#     else:
#         print(i)
#
# for i in range(20):
#
#     if i % 2 == 0:
#         continue
#     elif i == 17:
#         break
#     elif i == 15:
#         pass
#     else:
#         print(i, "is an odd number")
#
counter = 0
while True:
    if counter == 20:
        break
    elif counter % 3 == 0:
        counter += 1
        continue
    elif counter == 7:
        pass
    else:
        print(counter, "is not a multiple of 3")
    counter += 1

print("Loop has been broken at counter =", counter)

a = "Python"
a = ['apple', 'banana', 'cherry']
print(a[::-1])  # prints 'h', the character at index 3

















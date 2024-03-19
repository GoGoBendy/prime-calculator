"""Module providing a function printing prime numbers."""

# collecting a number from user
print("please input number for testing")
num = int(input())
# calling the function
DIVISABLE = int(0)
DIV = True
for DIVISABLE in range(2, num):
    if num % DIVISABLE == 0:
        DIVISABLE += 1
        DIV = False
    else:
        DIVISABLE += 1
if DIV is True:
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")

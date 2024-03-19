"""Module providing a function printing prime numbers."""

# collecting a number from user
print("please input number for testing")
num = int(input())
# calling the function
DIVISABLE = int(2)
for DIVISABLE in range(1, num):
    if num % DIVISABLE == 1:
        print(DIVISABLE)
        DIVISABLE += 1
    else:
        print(f"So far good {DIVISABLE}")
        DIVISABLE += 1

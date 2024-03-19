
#collecting a number from user
print("please input number for testing")
num = input()
num = int(num)
#calling the function
divisable = int(2)
for divisable in range(num):
    if num % divisable == 0:
        print(divisable)
        divisable + 1
    else:
        print(f"So far good {divisable}")
        divisable + 1
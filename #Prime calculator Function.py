
#collecting a number from user
print("please input number for testing")
num = int(input())
#calling the function
prime_calculator(num)
divisable = int(2)
for divisable in num:
    if num / divisable:
        print(divisable)
        divisable + 1
    else:
        divisable + 1
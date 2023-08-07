#Prime calculator Function
def prime_calculator(number):
    divisable = int(2)
    for divisable in number:
        if number / divisable:
            print(divisable)
            divisable + 1
        else:
            divisable + 1
    

#collecting a number from user
print("please input number for testing")
num = int(input())
#calling the function
prime_calculator(num)
end = input()
print("end")
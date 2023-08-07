#Prime calculator Function
def prime_calculator(number):
    divisable = 2
    for divisable in number:
        if number % divisable:
            print(divisable)
            divisable + 1
        else:
            divisable + 1
    

#collecting a number from user
num = input(print("Please input a number for testing"))
#calling the function
prime_calculator(num)
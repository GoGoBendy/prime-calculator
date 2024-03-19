"""Module providing a function printing prime numbers from a list."""


def prime(numb):
    """function providing list of primes from list"""
    div = True
    for divisable in range(2, numb):
        if numb % divisable == 0:
            divisable += 1
            div = False
        else:
            divisable += 1
    if div is True:
        print(f"{numb} is a prime")
    else:
        print(f"{numb} is not a prime")


# collecting a number from user
print("please input number for testing")
num = int(input())
# calling the function
print(prime(num))

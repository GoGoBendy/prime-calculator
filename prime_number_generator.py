"""Module providing a function generating prime numbers from a list."""


# function to return prime numbers from list
def prime(numlis):
    """function verifying if a number is prime"""
    numberlist = []
    numb = int(numlis)
    div = True
    for divisable in range(2, numb):
        if numb % divisable == 0:
            divisable += 1
            div = False
        else:
            divisable += 1
    if div is True:
        nume = str(numlis)
        numberlist.append(nume)
    numberliststr = " ".join(numberlist)
    return numberliststr


def generator(number):
    """function to send generated numbers for verification"""
    nums = 0
    numlist = []
    while nums != number:
        nono = prime(nums)
        if nono != "":
            numlist.append(prime(nums))
        nums += 1
    return ", ".join(numlist)


non = False
while non == False:
    # collecting a number from user
    num = int(input("what number would you like the generate primes to? "))
    if num == "exit":
        non = True
    # calling the function
    print(generator(num))

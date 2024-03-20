"""Module providing a function generating prime numbers from a list."""


# function to return prime numbers from list
def prime(num):
    """function providing list of primes generated"""
    numberlist = []
    numb = 1
    numbe = 0
    divisable = 0
    while numbe != num:
        div = True
        for divisable in range(2, numb):
            if numb % divisable == 0:
                divisable += 1
                div = False
                numbe += 1
            else:
                divisable += 1
                numbe += 1
        if div is True:
            numberlist.append(divisable)
    numberliststr = " ".join(numberlist)
    return numberliststr


# collecting a number from user
num = int(input("how many primes would you like to generate? "))
# calling the function
prime(prime(num))

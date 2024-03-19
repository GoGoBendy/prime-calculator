"""Module providing a function printing prime numbers from a list."""


# function to return prime numbers from list
def prime(numlis):
    """function providing list of primes from list"""
    numberlist = []
    for numbe in numlis:
        numb = int(numbe)
        div = True
        for divisable in range(2, numb):
            if numb % divisable == 0:
                divisable += 1
                div = False
            else:
                divisable += 1
        if div is True:
            numberlist.append(numbe)
    numberliststr = " ".join(numberlist)
    return numberliststr


# collecting a number from user
print("please input number for testing")
num = input()
if ", " in num:
    numlist = num.split(", ")
else:
    numlist = num.split(" ")
# calling the function
print(prime(numlist))

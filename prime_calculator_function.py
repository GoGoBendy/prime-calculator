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


NON = False
while NON is False:
    # collecting a number from user
    num = input("please input number for testing >")
    if ", " in num:
        numlist = num.split(", ")
    elif num == "exit":
        NON = True
    elif " " in num:
        numlist = num.split(" ")
    else:
        num2 = int(num)
        print(prime(num2))

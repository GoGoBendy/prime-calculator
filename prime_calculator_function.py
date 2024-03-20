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


non = False
while non == False:
    # collecting a number from user
    num = input("please input number for testing >")
    if ", " in num:
        numlist = num.split(", ")
    elif num == "exit":
        non = True
    else:
        numlist = num.split(" ")
    # calling the function
    prime(prime(numlist))

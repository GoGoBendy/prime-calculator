"""Module providing a function printing prime numbers from a list."""


# function to return prime numbers from list
def prime_function(numlis):
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


def function_call():
    """Function to call prime_function"""
    # collecting a number from user
    num1 = input("please input number for testing >")
    if ", " in num1:
        numlist = num1.split(", ")
    else:
        numlist = num1.split(" ")
    # calling the function
    prime_function(numlist)


# function to return prime numbers from list
def prime_generator(numlis):
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
        nono = prime_generator(nums)
        if nono != "":
            numlist.append(prime_generator(nums))
        nums += 1
    return ", ".join(numlist)


def generator_call():
    """function calling generator"""
    # collecting a number from user
    num2 = int(input("what number would you like the generate primes to? "))
    # calling the function
    print(generator(num2))


def generator_deluxe(number):
    """function to send generated numbers for verification"""
    nums = 0
    yesno = 0
    numlist = []
    while nums != number:
        nono = prime_generator(yesno)
        if nono != "":
            numlist.append(nono)
            nums += 1
        yesno += 1
    return ", ".join(numlist)


def generator_deluxe_cal():
    """functioh calling generator_deluxe"""
    # collecting a number from user
    num = int(input("how many primes would you like to generate? "))
    # calling the function
    print(generator_deluxe(num))


NON = False
while NON is False:
    numy = input("which program would you like to use? ")
    if numy == "calculator":
        print(function_call())
    elif numy == "generator":
        print(generator_call())
    elif numy == "generator deluxe":
        print(generator_deluxe_cal())
    elif numy == "exit":
        NON = True

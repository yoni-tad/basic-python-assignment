import random

# Question number one
def addPositiveNums():
    number = int(input("Enter positive number: "))
    if number > 0:
        result = 0
        for num in str(number):
            result += int(num)
        print(result)
    else:
        print("Please enter positive number only!")
        addPositiveNums()
# addPositiveNums()

# Question number two
def sumFactors():
    number = int(input('Enter a number: '))
    result = 0
    for i in range(1, number + 1):
        if number % i == 0:
            result += i
    print(result)

# sumFactors()

# Question number three
def randGame():
    randomNum = random.randrange(0, 100)
    userGuess = int(input("======== Welcome to Guess lucky Number Game ======== \nGuess the lucky number: "))
    tryCount = 0

    while True:
        if tryCount < 7:
            tryCount += 1
            if (userGuess == randomNum):
                print("Congratulation you Win, the lucky number is ", randomNum)
                break
            elif (userGuess > randomNum):
                userGuess = int(input("Guess less than " + str(userGuess) + ": "))
            elif (userGuess < randomNum):
                userGuess = int(input("Guess more than " + str(userGuess) + ": "))
        else:
            print("Game over, the lucky number is", randomNum)
            break

# randGame()

# Question number four
def findArmstrong():
    for num in range(0, 999):
        sum = 0
        for i in str(num):
            sum += int(i) ** 3
        if sum == num: 
            print(str(sum) + " is armstrong number")

# findArmstrong()
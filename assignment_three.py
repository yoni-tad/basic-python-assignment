# Question number one
def exclamation():
    strInput = str(input("Enter the string: "))

    vowelLetters = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for letter in strInput:
        if letter in vowelLetters:
            result.append(letter * 4)
        else:
            result.append(letter)
    result.append('!')
    print(''.join(result))

# exclamation()

# Question number two
def inversions():
    word = str(input("Enter the word: ")).upper()
    count = 0

    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] > word[j]:
                count += 1
    print(count)

# inversions()

# Question number three
def elevator():
    floor = 0
    askFloor = str(input(("where do you want to go: "))).lower()
    for i in askFloor:
        if i == '^':
            floor += 1
        elif i == 'v':
            if floor == 0:
                floor = 0
            else:
                floor -= 1
    print("You are in " + str(floor) + " floor")

# elevator()

# Question number four   
def largestDivisor():
    biggestDivisor = 1
    numOfDivisor = 1
    
    for num in range(1, 10000):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count > numOfDivisor:
            numOfDivisor = count
            biggestDivisor = num

    print("The largest number of divisors is " + str(biggestDivisor))
    print("It has " + str(numOfDivisor) + " divisors.")

largestDivisor()
# Question number one
def checkPalindrome():
    word = input("Enter the word: ")
    palindromeWord = ""

    for i in word:
        palindromeWord = i + palindromeWord
    
    if(word == palindromeWord):
        print("\"" + word +" \" is a palindrome")
    else:
        print("\"" + word +"\" is not a palindrome")

# checkPalindrome()

# Question number two
def wordCounter(sentence):
    sentence = sentence.split()
    wordCount = {}

    for word in sentence:
        if word in wordCount.keys():
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    print(wordCount)

# wordCounter("I ate an apple")

# Question number three
def removeStopWords(sentence):
    sentence = sentence.lower().split()
    stop_words = set(['a', 'an', 'the', 'and', 'is', 'in', 'on', 'at', 'to', 'of', 'for', 'with'])

    filterWords = []
    for word in sentence:
        if word not in stop_words:
            filterWords.append(word)
    print(' '.join(filterWords))

# removeStopWords("I ate an apple")
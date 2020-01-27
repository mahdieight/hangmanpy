import random
wordsArr = [
    'facebook',
    'youtube',
    'telegram',
    'google',
    'yahoo',
    'digikala',
    'alibaba',
]

selectedItem = random.choice(wordsArr)
lenSelectedItem = len(selectedItem)
isComplated = False
failCounter = 0
wordsInItem = []
wordSayUser = []
print("The word you have selected has", lenSelectedItem, " words", "")

for word in list(selectedItem):
    if (word not in wordsInItem):
        wordsInItem.append(word)

while (failCounter < lenSelectedItem and not isComplated):
    print("Please enter a word :) ")
    userInput = raw_input()
    if (len(userInput) > 1):
        print("Just one word!")
        continue
    elif (userInput in selectedItem):
        if (userInput not in wordSayUser):
            wordSayUser.append(userInput)
        if (len(wordsInItem) == len(wordSayUser)):
            isComplated = True
            print("Well you won")

        exportStr = ''
        for x in list(selectedItem):
            if (x not in wordSayUser):
                exportStr += ' - '
            else:
                exportStr += ' ' + x + ' '
        print(exportStr)
    else:
        failCounter += 1
        print("It was wrong - Number of times allowed :",
              lenSelectedItem - failCounter)

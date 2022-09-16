# Check if your word matches the array, you get 2 attempts

someList = ['Hi', 'How', 'Are', 'You']

def wordPrinter(item, index):
    print(f'Your Matching Word: "{item}", At Index: {index + 1}')


def checkForMatch(word):
    for index, item in enumerate(someList):
        if item.lower() == word.lower():
            wordPrinter(item, index)
            return
        print('Sorry, We Have Found No Match')
        retry = input('Try Again: ')
        for item in someList:
            if item.lower() == retry.lower():
                print('Match On The Second Attempt!')
                return    
            print('Sorry, Still No Match')
            return


userQuestion = input('What is your word? ')
checkForMatch(userQuestion)


from random import randint

isPlayed = False
def getinput():
    try:
        guessedNumber = int(input())
        return guessedNumber
    except:
        print("Enter a valid number")
        return None
        

def guessGame():
    global isPlayed
    generated_number = randint(1,10)
    isPlayed = True
    for i in range(5):
        while(True):
            print("Enter your guessed number: ")
            guessedNumber = getinput()
            if guessedNumber in range(1,11):
                difference = abs(guessedNumber-generated_number)
                if difference == 0:
                    print('Its a match! Congrats')
                    return
                elif difference in [9, 8]:
                    positon = 'very cold'
                elif difference in [7, 6]:
                    positon = 'cold'
                elif difference in [5, 4]:
                    positon = 'neutral'
                elif difference == 3:
                    positon = 'warm'
                elif difference < 2:
                    positon = 'hot'    
                if guessedNumber < generated_number:
                    print(f'Your guess is cold from left and {positon} from right. Try again')
                else:
                    print(f'Your guess is {positon} from left and cold from right. Try again')
                break
            elif guessedNumber is None:
                continue
            else:
                print("Enter a number in the range (0,10)")
                continue

while(True):
    print('1. Play again' if isPlayed else '1. Start the Game')
    print('2. Exit')
    
    print("Enter the required option")
    option = getinput()
    
    if option:         
        match option:
            case 1: guessGame()
            case 2: break
            case _: print('Invalid option')
    else:
        continue
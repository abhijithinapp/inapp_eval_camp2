from random import randint
print("""------Welcome to RockPaper Scissors game--------------
You will have 5 chances and the person having most points will win
Points are assigned as per following rules
Rock beats scissors
Scissors beats paper
Paper beats rock
""")


#function returns 'h' if winner is human and 'c' if winner is computer 't' if tie
def findWinnerOfChance(humanPlayer,computerPlayer):
    if humanPlayer == computerPlayer:
        return 't'
    elif humanPlayer == 1 and computerPlayer==2:
        return 'c'
    elif humanPlayer == 1 and computerPlayer==3:
        return 'h'
    elif humanPlayer == 2 and computerPlayer == 1:
        return 'h'
    elif humanPlayer == 2 and computerPlayer == 3:
        return 'c'
    elif humanPlayer == 3 and computerPlayer == 1:
        return 'c'
    elif humanPlayer == 3 and computerPlayer == 2:
        return 'h'

def printWinnerofGame(computerPoints, humanPoints):
    print("""
    
    -----Game Over!!-----
Computer's Points: {}
Your Points: {}""".format(computerPoints,humanPoints))
    if computerPoints == humanPoints:
        print("It was a tie")
    elif computerPoints > humanPoints:
        print("Computer won the game")
    else:
        print("You won the Game")
        

computerPoints = 0
humanPoints = 0
i=0
while(i<5):
    humanPlayer=int(input("""
Enter the value assigned to your choice
1. Rock
2. Paper
3. Scissors
"""))
    computerPlayer = randint(1,3)
    print("Your Choice: {}\nComputer's Choice: {}".format(humanPlayer,computerPlayer))
    winner = findWinnerOfChance(humanPlayer,computerPlayer)
    match(winner):
            case 't': print("It was a tie. No one gets points")
            case 'h':
                print("You won in this chance!! You got one point.")
                humanPoints = humanPoints + 1
            case 'c': 
                print("Computer won in this chance!! Computer got one point.")
                computerPoints=computerPoints+1
    i = i+1
printWinnerofGame(computerPoints,humanPoints)





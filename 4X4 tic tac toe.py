import os
s=input("Enter your name User 1: ")
q=input("Enter your name User 2: ")
def printBoard(gameValues):
    # Printing Board By using gameValues 's List
    print(f"  {gameValues[0]}  |  {gameValues[1]}  |  {gameValues[2]}  |  {gameValues[3]}")
    print(f"-----|-----|-----|-----")
    print(f"  {gameValues[4]}  |  {gameValues[5]}  |  {gameValues[6]}  |  {gameValues[7]}")
    print(f"-----|-----|-----|-----")
    print(f"  {gameValues[8]}  |  {gameValues[9]}  |  {gameValues[10]} |  {gameValues[11]}")
    print(f"-----|-----|-----|-----")
    print(f" {gameValues[12]}  |  {gameValues[13]} |  {gameValues[14]} |  {gameValues[15]}")

def checkWin(gameValues):
    # All Winning Patterns
    wins = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [0, 5, 10, 15], [3, 6, 9, 12]]

    for win in wins:
        # if gameValues matches with the pattern and has X then X won the Match
        if(gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == gameValues[win[3]] == 'X'):
            printBoard(gameValues)
            print(s,"Won the match")
            print("Better luck next time",q)
            return 1

        # if gameValues matches with the pattern and has X then O won the Match
        if(gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == gameValues[win[3]] == 'O'):
            printBoard(gameValues)
            print(q,"Won the match")
            print("Better luck next time",s)
            return 0

        # if all places are filled and no one is the winner
        if all(isinstance(item, str) for item in gameValues):
            printBoard(gameValues)
            return -2
    # return -1 if no one wins
    return -1

if __name__ == '__main__':
    print("Welcome to the Game",s,"and",q)
    print("Good luck!")
    gameValues=[0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12, 13, 14, 15]
    chance = 1

    while(True):
        try:
            if chance == 1:
                printBoard(gameValues)
                print("\nIt's your Chance",s)
                value = int(input("\nPlease enter a value: \n"))

                # check if already filled with O
                if gameValues[value]!= 'O':
                    gameValues[value] = 'X'
                else:
                   
                    print("\nPlease Enter Different Location for X\n")
                    continue
                

            if chance == 0:
                printBoard(gameValues)
                print("\nIt's your Chance",q)
                value = int(input("\nPlease enter a value: \n"))

                # check if already filled with X
                if gameValues[value]!= 'X':
                    gameValues[value] = 'O'
                else:
                   
                    print("\nPlease Enter Different Location for O\n")
                    continue
               

        except IndexError:
            # exception if Value is not between 0 to 15 
            
            print("\nOops!! Please Enter value from 0 - 15\n")
            continue

        # for giving chance to other player
        chance = 1 - chance
        cwin = checkWin(gameValues)
        # Game Draw
        if(cwin == -2):
            print("Phew!It's a draw.\nWhat a match. Looks like you both are geniuse!!.")
            break
        # Match Over
        if(cwin != -1):
            print("Congratulations on your win!!")
            break

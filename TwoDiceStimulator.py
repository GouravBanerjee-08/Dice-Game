def display(n):
    if(n==1):
        print(" ----------")
        print("|          |")
        print("|    O     |")
        print("|          |")
        print(" ----------")
        
    if(n==2):
        print(" ----------")
        print("|          |")
        print("|  O   O   |")
        print("|          |")
        print(" ----------")
    
    if(n==3):
        print(" ----------")
        print("|     O    |")
        print("|     O    |")
        print("|     O    |")
        print(" ----------")
    if(n==4):
        print(" ----------")
        print("|  O   O   |")
        print("|          |")
        print("|  O   O   |")
        print(" ----------")
    if(n==5):
        print(" ----------")
        print("|  O   O   |")
        print("|    O     |")
        print("|  O   O   |")
        print(" ----------")
    if(n==6):
        print(" ----------")
        print("|   O  O   |")
        print("|   O  O   |")
        print("|   O  O   |")
        print(" ----------") 
import random
print("WELCOME TO THE DICE GAME\nIn this game 2 dice are rolled by Player 1 and Player 2 respectively.\nThe player to get a Doublet first,WINS")
print("Press r to roll the two dice again.")
print("Press any key to quit the game.")
print("1st PLAYER's TURN")
x=input()
while(x=='r'):
    v1=random.randint(1,6)
    v2=random.randint(1,6)
    display(v1)
    display(v2)
    if(v1==v2):
        print("1st PLAYER WINS")
        break
    else:
        print("2nd PLAYER's TURN")
        y=input()
        if(y=='r'):
            v3=random.randint(1,6)
            v4=random.randint(1,6)
            display(v3)
            display(v4)
            if(v3==v4):
                print("2nd PLAYER WINS")
                break
            else:
                print("1st PLAYER's TURN")
                x=input()
        else:
            break
if(x!='r' or y!='r'):
    print("GAME OVER!")

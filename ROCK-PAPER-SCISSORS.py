# ROCK PAPER SCISSORS GAME WITH COMPUTER
print(" ")

import random

def play():
    user=input("WHAT IS YOUR CHOICE : r for rock, p for Paper, s for Scissors : \n")
    computer=random.choice(['r','p','s'])
    
    if user==computer:
        return ' Its a Tie !'
   
    if winner(user, computer):
        return 'YOU WON ! '
 
    return 'YOU LOST ! '
# r>s , s>p , p>r

#Irrespective of user or computer , the winner needs a justifiable algorithm
def winner(player,opponent):
    
    if (player == 'r'and opponent == 's') or (player == 'p'and opponent == 'r')  or (player == 's'and opponent == 'p') :
        return True
    
print(play())


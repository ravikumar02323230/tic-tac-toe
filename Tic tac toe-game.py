#!/usr/bin/env python
# coding: utf-8

# ## Tic-Tac-Toe

# In[1]:


#3 by 3 board representation.
from IPython.display import clear_output

def display_board(board):
    clear_output() # works in jupiter for any IDE use print('/n*100')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('---|---|---')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('---|---|---')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    
    pass


# In[2]:


#player input
def player_input():
    while True:
        i=input('Do you want to be X or O, zyadatar londe X hi lete h').upper()
        if i=='X':
            player1='X'
            player2='O'
            return player1, player2
        elif i=='O':
            player1='O'
            player2='X'
            return player1, player2
        else:
            continue
    
    
    pass


# In[3]:


#desired position (number 1-9)
def place_marker(board, marker, position):
    #position = int(position)
    board[position] = marker
    pass


# In[4]:


#checks to see if that mark has won
def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
        #break
    elif board[4] == board[5] == board[6] == mark:
        return True
        #break
    elif board[7] == board[8] == board[9] == mark:
        return True
        #break
    elif board[1] == board[4] == board[7] == mark:
        return True
        #break
    elif board[2] == board[5] == board[8] == mark:
        return True
        #break
    elif board[3] == board[6] == board[9] == mark:
        return True
        #break
    elif board[1] == board[5] == board[9] == mark:
        return True
        #break
    elif board[3] == board[5] == board[7] == mark:
        return True
        #break
    else:
        return False
    pass


# In[5]:


# randomly decide which player goes first
import random

def choose_first():
    r = random.randint(1,2)
    if r == 1:
        return 'Player 1'
    elif r ==2:
        return 'Player 2'
    pass


# In[6]:


#whether a space on the board is freely available
def space_check(board, position):
    return board[position] == ' '
    pass


# In[7]:


#Checks if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    pass


# In[8]:


#asks for a player's next position 
def player_choice(board):
    '''position = int(input('Enter your next position(1-9):'))
    while space_check(board, position):
        return position'''
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position, teri chance h chal: (1-9) '))
        
    return position
    pass


# In[9]:


#if the player want to play again
def replay():
    k= input('Khelega dobara (YES/NO)').upper()
    if k == 'YES':
        return True
    elif k == 'NO':
        return False
    pass


# In[10]:


print('Welcome to Tic Tac camel-toe aka maut ka nanga-nach!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first kyuki bakchod h.')
    
    play_game = input('Are you ready to play, khelega na pakka? Yes ya No bol jaldi')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Sheeeeeeeeeeesh! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw, lode lg gye dono ke!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won, as if we care!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw, lode lg gye')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:





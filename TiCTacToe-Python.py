#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Displaying the Board
def display(row):
    print('|__{}__|__{}__|__{}__|'.format(row[0],row[1],row[2]))
    print('|__{}__|__{}__|__{}__|'.format(row[3],row[4],row[5]))
    print('|__{}__|__{}__|__{}__|'.format(row[6],row[7],row[8]))
    #print(row[0:3])
    #print(row[3:6])
    #print(row[6:9])


# In[2]:


#Chosing X or O
#Accepting Input
#Steps player 1 input validate
#Add to the array 
#Check
#Steps player 2 input validate
#Add to the array 
#Check for win


# In[3]:


#Player 1 Choses X or O
def choice_letter():
    letter1 = "k"
    while letter1.lower() not in ['o','x']:
        letter1 = input("Hello and Welcome Player 1 -  Please choose either x or o: ")
    if letter1.lower() == 'x':
        letter2 = 'o'
    else:
        letter2 = 'x'
    return letter1,letter2


# In[4]:


#Choosing the Position
def position_record(row,player):
    position = 'p'
    within_range = False
    not_filled = False
    
    while position.isdigit() == False or within_range == False or not_filled == False:
        position = input(f'{player} - Please choose an position where you want to add your letter: ')
        
        #Error message if it's not a digit
        if position.isdigit() == False:
            print("Please enter a valid integer")
            
        #Error message if it's not in range    
        elif int(position) not in range(1,10):
            print("Please enter a number between 1- 9: ")
            within_range = False
            
        elif row[int(position)-1] in ['x','o']:
            print("Position already full. Please choose an empty position")
            not_filled = False
        else:
            within_range = True
            not_filled = True
            
            
            
    return int(position)
            
        
            
    


# In[5]:


#Adding to the element to the list based on the player choice
def add_position(position,player_alphabet,row):
    row[position-1]=player_alphabet
    return row


# In[6]:


#Check Win Conditions
def check_complete(row,player):
    if (len(set(row[0:3]))==1 or len(set(row[3:6]))==1 or len(set(row[6:9]))==1 or len(set(row[0:9:3]))==1 or len(set(row[1:9:3]))==1 or len(set(row[2:9:3]))==1 or len(set(row[0:9:4]))==1 or len(set(row[2:8:2]))==1):
        if player == 1:
            clear_output()
            print("Player 1 wins")
            return True
        else:
            clear_output()
            print("Player 2 wins")
        return True
    elif len(set(row))==2:
        clear_output()
        print("Game Tied")
        return True
    else:
        return False
    


# In[7]:


def gameon_choice():
    choice = "WRONG"
    while choice.lower() not in ['y','n']:
        choice = input("Keep Playing? (y or n) ")
        
        if choice.lower() not in ['y','n']:
            print("Sorry, I don't understand, please choose y or n ")
            
    return choice == "y"


# In[8]:


#Main Program
from IPython.display import clear_output
game_on = True
while game_on:
    row = [1,2,3,4,5,6,7,8,9]
    
    #Alphabet assignment to players
    p1_choice,p2_choice = choice_letter()
    
    #Intialising the variable complete used to check if the game is complete (win/tied)
    complete = False
    
    #Continue asking for input while the game is not complete
    while complete == False:
        clear_output()
        display(row)
        position1 = position_record(row,'Player1')
        row = add_position(position1,p1_choice,row)
        complete = check_complete(row,1)
        #Check and break out of the loop if game finishes after player1's move
        if complete:
            break
            
        clear_output()
        display(row)
        position2 = position_record(row,'Player2')
        row = add_position(position2,p2_choice,row)
        complete = check_complete(row,2)
        #Check and break out of the loop if game finishes after player2's move
        if complete:
            break
    
    display(row)        
    print("Game Over")
    game_on = gameon_choice()
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





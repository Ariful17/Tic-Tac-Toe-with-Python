from random import choice


display=[ "_","_","_",            #This is for the grid display for tic tac toe, total 9 spaces
          "_","_","_",
          "_","_","_" ]

game_finished=False               #a global boolean variable for iterating the main function until someone wins or draw takes place
global state                      #a global boolean variable - decides whose turn it is, "X" or "O"
repeat=True                       #a global boolean variable to start a new game
found=False

list= ["1", "2","3","4","5","6","7","8","9"]         #list of possible all position number in grid display

def play_game():                  #the main function
    global state                  #declaring the global boolean variable inside this function

    choice=input("\nChoose your first input- 'x' or 'o'\n")             #a choice input for the first turn, only for the first time

    while choice!='x' and choice!='o':                                  #checking the input
        choice=input("\nPlease choose either of them- 'x' or 'o'\n")    #again asking for an input
        if choice=='x' or choice=='o':                                  #if the input matches stop the loop
            break


    board()                       #calls the board function which shows the grid display of tic tac toe

    if choice=='x':               #set the value of "state" variable depending on your first input
        state=True                #here for "X" the state will always be in true condition and for "O" vice versa
    else:
        state=False               
     
    while game_finished!=True:                      #until the game reaches to an end, the value of this variable will be False
        write()                                     #and it will enter this while loop, once the value is true, it wont anymore
        check_if_finished()                         #calls two funtion- one is for writing "X"/"O"
                                                    #and ither fir checking if it has reached an end
        if check_if_finished:                       #if it has reached to an end, this function will return a value and we will assign
            winner=check_if_finished()              #it to a variable called winner, basically whoever wins or if there's draw- this
                                                    #function will give that to us
    print("\nGame is over\n")                                  #prints a line
    if winner=="X" or winner=="O":                             #checks who is the winner    
        print("Winner is "+ winner+"\n")
    else:
        print("It's a Draw\n")                                 #if the result is neither "X" nor "O" it's a draw


def board():
    print(display[0] + " |  " + display[1] + " |  " + display[2])           #the board function which prints the grid display
    print(display[3] + " |  " + display[4] + " |  " + display[5])           #we are calling the elements from display list
    print(display[6] + " |  " + display[7] + " |  " + display[8])           #print it and you will get the visualization


def write():                                  #Here is the details of write function
    global state                              #declaring the global variable, otherwise it won't recognize
    index=take_input()                        #whatever the "take input()" function returns we store it in index variable
    global found

    if state:                                          
        display[index]='X'                    #if boolean "state" variable is true than we print X, see comment of line 17                               
        state=False                           #after X we need someone to write O, for that we change the state variable to false
    else:                                          
        display[index]='O'                    #or if the state is false we print O and for the next X turn changing the state true                                    
        state=True

    board()                                   #we again call the board function to print our updated grid display
    found= False                              #a variable to shuffle between human move and computer move
    computerMove()                            #now the computer move


def take_input():                                                         #this function is for taking user input- "X" or "O"

    validInput=False                                                      #setting it false

    position= input("Choose a position from 1-9\n")                       #in which position we want to write our "X or "O"

    while(validInput!=True):                                                  #until condition for valid Input is fulfilled

        while position not in list:                                           #if we enter an invalid position number it will 
            position= input("Invalid input, Choose a position from 1-9\n")    #ask again to input a valid number
        
        if display[int(position)-1]!="_":                                     #if we enter a position number that's already been used
            print("This position is already taken")                           
            position= input("Choose a new position from 1-9\n")               
            validInput=False
        else:
            validInput=True                                                   #condition fulfilled

        
    position=int(position)-1                            #we take the input as string, but for a position in display list we need
    return position                                     #an index and index number is integer, so we convert it. the index starts from 0
                                                        #but we are taking position input from number 1, so need to subtract -1

def check_if_finished():                           #this function is for checking any result or draw
    row_winner=check_rows()                        #checks if any row has matched
    column_winner=check_columns()                  #checks if any column has matched
    diagonal_winner=check_diagonals()              #checks if any diagonal has matched
    draw=check_draw()                              #check if there's a draw

    if row_winner:                      #if any row is matched, returns the winner whether it's "X" or "O"
        return row_winner
    if column_winner:                   #does the same work as previous line
        return column_winner    
    if diagonal_winner:                 #does the same work as previous line
        return diagonal_winner
    if draw:                            #if there's a match for draw, returns that it's a draw
        return draw


def check_rows():                                        #this function is for row checking

    global game_finished                                 #declaring the global variable to use inside here

    row_1= display[0]==display[1]==display[2]!="_"       #if there's a common element in the first row (except the underscore which is
    row_2= display[3]==display[4]==display[5]!="_"       #present from the beginning as a blank indicator)
    row_3= display[6]==display[7]==display[8]!="_"       #same for 2nd and 3rd row

    if row_1 or row_2 or row_3:                          #if any of above line is logically true it means the game is finished
        game_finished=True                               #so we change the value of this global boolean variable to true

    if row_1:                                            #if first row is matched than we return an element of first row as the winner
        return display[0]
    if row_2:                                            #same for 2nd and 3rd row
        return display[3]   
    if row_3:
        return display[6]
  

def check_columns():                                     #this function is for checking the columns

    global game_finished

    column_1= display[0]==display[3]==display[6]!="_"    #everything is as same as the row function, here it's column instead of row
    column_2= display[1]==display[4]==display[7]!="_"
    column_3= display[2]==display[5]==display[8]!="_"    #you can relate rest of the lines to previous function
    
    if column_1 or column_2 or column_3:
        game_finished=True        
    
    if column_1:
        return display[0]
    if column_2:
        return display[1]   
    if column_3:
        return display[2]


def check_diagonals():                                     #this function is for checing the diagonals

    global game_finished

    diagonal_1= display[0]==display[4]==display[8]!="_"    #again everything is same as before, here are just two diagonals
    diagonal_2= display[2]==display[4]==display[6]!="_"
    
    if diagonal_1 or diagonal_2:
        game_finished=True 

    if diagonal_1:
        return display[0]
    if diagonal_2:
        return display[2] 


def check_draw():                        #this functions checks for a draw

    global game_finished                 #declaring the global variable as we will use it inside here

    if "_" not in display:               #if there's no underscore(which indicates blank space) present inside the display list it
        game_finished=True               #means all the element spaces are occupied by either "X" or "O" and still there
        return "draw"                    #are no row,column or diagonal matches. So from the game rule we can say that it's a draw.
                                         #so we return a string called "draw"



def computerMove():                      #function for computer move

    global game_finished
    global state
    global found

    possibleMove=[]                                     #all possible move
    for i in range(len(display)):
        if '_'==display[i]:
            possibleMove.append(i)                      #storing the empty places in an array

    if state:
        list_order=['X','O']                            #checking firstly- if computer can win with next move, if so carry out the move and win
    else:
        list_order=['O','X']                            #         secondly- if human can win with next move, if so block the move by placing there

    for letter in list_order:

        for i in possibleMove:
            
            display[i]=letter

            if check_if_finished():

                game_finished=False

                if state:                                          
                    display[i]='X'                                                  
                    state=False                          
                else:                                          
                    display[i]='O'                    
                    state=True 
                print("\nMove of the computer:\n")
                board()
                found=True
                break

            else:
                display[i]='_'
        if found:
            break


    if found!=True:                               #if no winning or loosing situation, place the move in center
        if display[4]=='_':
            if state:                                          
                display[4]='X'                                                  
                state=False                          
            else:                                          
                display[4]='O'                    
                state=True 
            found=True
            print("\nMove of the computer:\n")
            board()

    # if algorithm_for_cornerMove1():               #print test to be sure if the algorithms are working
    #     print("\ntruecornerways1\n")              #6 types of algorithm to prevent loosing

    # if algorithm_for_cornerMove2():
    #     print("\ntruecornerways2\n")

    # if algorithm_for_sideMove1():
    #     print("\ntrueSideways1\n")

    # if algorithm_for_sideMove2():
    #     print("\ntrueSideways2\n")
    
    # if algorithm_for_sideMove3():
    #     print("\ntrueSideways3\n")

    # if algorithm_for_sideMove4():
    #     print("\ntrueSideways4\n")

    if found!=True:                                                                          #if center is occupied, look for corner positions
        if algorithm_for_cornerMove1()!=True and algorithm_for_cornerMove2()!=True:          #to prevent loosing, avoid corner move for this case 
            cornerMove=[]
            for i in [0,2,6,8]:                                                              #collect empty diagonal positions
                if display[i]=='_':
                    cornerMove.append(i)                                                     
            
            if algorithm_for_sideMove1()==True:                                              #remove specific corner position to avoid loosing
                cornerMove.remove(6)                                                         #4 types of algorithm to avoid this

            if algorithm_for_sideMove2()==True:
                cornerMove.remove(0)

            if algorithm_for_sideMove3()==True:
                cornerMove.remove(2)

            if algorithm_for_sideMove4()==True:
                cornerMove.remove(8)
            
            if len(cornerMove)!=0:
                import random
                random_select=random.choice(cornerMove)                  #randomly select any empty corner position
                if state:                                          
                    display[random_select]='X'                                                  
                    state=False                          
                else:                                          
                    display[random_select]='O'                    
                    state=True 
                found=True
                print("\nMove of the computer:\n")
                # print("\ncornermove\n")           #print test to be sure of corner move
                board()        

    if found!=True:                                         #if no corner position is available, look for possible sideway positions
        sideMove=[]
        for i in [1,3,5,7]:                                 #collect all possible sideway positions
            if display[i]=='_':
                sideMove.append(i)
        
        if len(sideMove)!=0:
            import random
            random_select=random.choice(sideMove)           #randomly select any sideway position
            if state:                                          
                display[random_select]='X'                                                  
                state=False                          
            else:                                          
                display[random_select]='O'                    
                state=True 
            found=True
            print("\nMove of the computer:\n")
            # print("\nsidemove\n")                  #print test to be sure of side move
            board()  

#6 different algorithms below to prevent loosing, you can understand them by drawing the positions and figuring out the possible situations of loosing a game

def algorithm_for_cornerMove1():
    diagonal_position_1=display[0]==display[8]!='_' and display[4]!='_' and display[4]!=display[0] and display[1]==display[2]==display[3]==display[5]==display[6]==display[7]=='_'
    return diagonal_position_1       #avoid corner move

def algorithm_for_cornerMove2():
    diagonal_position_2=display[2]==display[6]!='_' and display[4]!='_' and display[4]!=display[2] and display[0]==display[1]==display[3]==display[5]==display[7]==display[8]=='_'
    return diagonal_position_2       #avoid corner move

def algorithm_for_sideMove1():
    side_position_1=display[1]==display[5]!='_' and display[4]!='_' and display[4]!=display[1] and display[0]==display[2]==display[3]==display[6]==display[7]==display[8]=='_'
    return side_position_1     #avoid display[6]

def algorithm_for_sideMove2():
    side_position_2=display[5]==display[7]!='_' and display[4]!='_' and display[4]!=display[5] and display[0]==display[1]==display[2]==display[3]==display[6]==display[8]=='_'
    return side_position_2     #avoid display[0]

def algorithm_for_sideMove3():
    side_position_3=display[3]==display[7]!='_' and display[4]!='_' and display[4]!=display[7] and display[0]==display[1]==display[2]==display[5]==display[6]==display[8]=='_'
    return side_position_3     #avoid display[2]

def algorithm_for_sideMove4():
    side_position_4=display[1]==display[3]!='_' and display[4]!='_' and display[4]!=display[3] and display[0]==display[2]==display[5]==display[6]==display[7]==display[8]=='_'
    return side_position_4    #avoid display[8]

while repeat:
                                                             #this while loop is for another game, continous playing
    play_game()                                              #at the very beginning this function is executed and we play for the
                                                             #first time
    further=input("Do you want to play again? (y/n)\n\n")    #after the first game it asks for another game
    if further=="y":                                        

        display=[ "_","_","_",          #if the answer is yes it clears the display list making it blank again
          "_","_","_",
          "_","_","_" ]

        game_finished=False             #and it changes the value of this boolean variable to false

        repeat=True                     #by keeping this value true, we stay inside this while loop
                                        #and the play_game function is executed again, meaning we are playing again
    else:                                            
        print("\nThank you\n\n")        #if you input no or anything other than "y" it will print this message and change the
        repeat=False                    #value of repeat variable to false which will cause the process to exit the loop.




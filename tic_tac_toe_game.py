display=[ "_","_","_",            #This is for the grid display for tic tac toe, total 9 spaces
          "_","_","_",
          "_","_","_" ]

game_finished=False               #a global boolean variable for iterating the main function until someone wins or draw takes place
global state                      #a global boolean variable - decides whose turn it is, "X" or "O"
repeat=True                       #a global boolean variable to start a new game

def play_game():                  #the main function
    global state                  #declaring the global boolean variable inside this function

    choice=input("\nChoose your first input- 'X' or 'O'\n")        #a choice input for the first turn, only for the first time

    board()                       #calls the board function which shows the grid display of tic tac toe

    if choice=='X':               #set the value of "state" variable depending on your first input
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

    if state:                                          
        display[index]='X'                    #if boolean "state" variable is true than we print X, see comment of line 17                               
        state=False                           #after X we need someone to write O, for that we change the state variable to false
    else:                                          
        display[index]='O'                    #or if the state is false we print O and for the next X turn changing the state true                                    
        state=True

    board()                                   #we again call the board function to print our updated grid display


def take_input():                                                         #this function is for taking user input- "X" or "O"

    position= input("Choose a position from 1-9\n")                       #in which position we want to write our "X or "O"

    while position not in ["1", "2","3","4","5","6","7","8","9"]:         #if we enter an invalid position number it will 
        position= input("Invalid input, Choose a position from 1-9\n")    #ask again to input a valid number

    while display[int(position)-1]!="_":                                  #if we enter a position number that's already been used
        print("This position is already taken, choose a new one")         #that first line is bit tricky but you'll get it 
        position= input("Invalid input, Choose a position from 1-9\n")    #after few lines
        
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




#========================================================================================#
#                                                                                        #
#                               THE TIC TAC TOE MACHINE 2.0                              #
#                                                                                        #
#                                     BY ZACK ZHANG                                      #
#                                                                                        #
#========================================================================================#

#Note: this version of the tic-tac-toe machine uses a new algorithm that produces more
#random moves and allows the player to win against the computer if moves are carefully
#chosen. 

#This is the lists of moves that the computer may make, in order or urgency
winning_square=[]
urgent_square=[]
other_square=[]
import random


#This will visually represent the tic tac toe board
def print_board():
    print ("               "+ str(board[0]) +" | " +str(board[1]) +" | " +str(board[2]))
    print ("               "+ "---------")
    print ("               "+ str(board[3]) +" | " +str(board[4]) +" | " +str(board[5]))
    print ("               "+ "---------")
    print ("               "+ str(board[6]) +" | " +str(board[7]) +" | " +str(board[8]))
    

#This makes sure they know the rules, and wants to enter the match
def player_confirmation ():
    print("""You will be playing Tic-Tac-Toe against a machine.
    This will be your checkerboard.
    Enter the corresponding number in each of the grids to place your piece.
    You will move first.
    I will be using "O" and you will be using "X".""")
    print_board()
    intention=False
    while intention==False:
        confirmation=input ("""Please confirm you know the rules by typing "Yes".
Or you may exit the match by typing "No". """).strip().capitalize()
        if confirmation=="Yes":
            print ("Match Begins!")
            intention=True
            return True
        elif confirmation=="No": 
            print ("""You will not be able to enter the match.""")
            break
        else:
            print ("""Response invalid! You may only enter "Yes" or "No".""")


#This function classifies if a winning square or an urgent square is present
#within a select row
def check_row(a,b,c):
    sorted_row = sorted([board[a],board[b],board[c]])
    if sorted_row [1:]==["O" ,"O"]:
        if sorted_row [0] not in ["O", "X"]:
            if board[a] not in ["O", "X"]:
                winning_square.append(str(a+1))
            elif board[b] not in ["O", "X"]:
                winning_square.append (str(b+1))
            elif board[c] not in ["O", "X"]:
                winning_square.append (str(c+1))
    elif sorted_row[ 1:]==["X", "X"]:
        if sorted_row [0] not in ["O", "X"]:
            if board[a] not in ["O", "X"]:
                urgent_square.append(str(a+1))
            elif board[b] not in ["O", "X"]:
                urgent_square.append (str(b+1))
            elif board[c] not in ["O", "X"]:
                urgent_square.append (str(c+1))


#This applies the check_row function to all straight 3-square rows
def check_all_rows():
    check_row (0,1,2)
    check_row (3,4,5)
    check_row (6,7,8)
    check_row (0,3,6)
    check_row (1,4,7)
    check_row (2,5,8)
    check_row (0,4,8)
    check_row (2,4,6)
    check_other_spots()

    
#This removes the duplicate in winning squares and urgent squares, and also
#checks for the other possible moves.
def check_other_spots():
    for item in urgent_square:
        urgent_square.remove(item)
        if item not in urgent_square:
            urgent_square.append (item)
    for item in winning_square:
        winning_square.remove(item)
        if item not in winning_square:
            winning_square.append (item)
    for item in ["1","2","3","4","5","6","7","8","9"]:
        if item in board:
            if item  not in winning_square:
                if item  not in urgent_square:
                    if item not in other_square:
                        other_square.append (item)



#This function is called when computer makes a move
def move (moves): 
    placement=random.randint(0,len(moves)-1)
    number=moves [placement]
    print ("I will put my piece on " + str(number) + ".")
    board[int(number)-1]="O"

    
#Computer will first prioritize a winning move (when computer lands there, it will win).
#The second order of priority are the urgent move(if computer doesn't land there, player
#can win by landing there in the next move). The last order of priority are the other
#squares, which will not let either side win if their piece is placed on it.
def computer_move():
    check_all_rows()
    if winning_square!=[]:
        move (winning_square)
    elif urgent_square!=[]:
        move (urgent_square)
    else:
        move (other_square)
    del winning_square[:]
    del urgent_square[:]
    del other_square[:]
    print_board()



#Prompts the player to place in a grid, and makes sure the grid is not taken
def player_move():
    valid=False
    while valid==False:
        entry=(input ("Enter the number where you would like to place the piece:  ").strip())
        if entry not in ["1","2","3","4","5","6","7","8","9"]:
            print ("Entry invalid! You must enter a number between 1 and 9 that corresponds with the spots on the board.")
        else:
            if entry not in board:
                print ("The spot you have chosen has already been taken. Choose another spot.")
            else:
                entry=int(entry)
                board[entry-1]="X"
                print ("You place your piece on " + str(entry)+"." )
                print_board()
                valid=True
                return entry



#This checks if the win condition has been met. If it has, then the game ends.
def keep_playing():   
    if board[0:3]==["X","X","X"] or board[3:6]==["X","X","X"] or board[6:9]==["X","X","X"]\
       or board[0:7:3]==["X","X","X"] or board[1:8:3]==["X","X","X"] or \
       board[2:9:3]==["X","X","X"] or board[0:9:4]==["X","X","X"] or board[2:7:2]==["X","X","X"]:
        return False
    elif board[0:3]==["O","O","O"] or board[3:6]==["O","O","O"] or board[6:9]==["O","O","O"]\
       or board[0:7:3]==["O","O","O"] or board[1:8:3]==["O","O","O"] or \
       board[2:9:3]==["O","O","O"] or board[0:9:4]==["O","O","O"] or board[2:7:2]==["O","O","O"]:
        return False
    else:
        return True


#This is the algorithm when the player chooses to go first
def ttt_player_first():
    counter=0
    while True and (counter <9):
        player_move()
        counter+=1
        if keep_playing()==True and (counter <9):
            computer_move()
            counter+=1
            if keep_playing()==True and (counter <9):
                pass
            else:
                print ("I win!")
                return False
        elif keep_playing()==False:
            print("You win!")
            return False
        elif counter >= 9:
            print ("Draw!")
            return False

#This is the algorithm when the computer goes first
def ttt_computer_first():
    counter=0
    while True and (counter <9):
        computer_move()
        counter+=1
        if keep_playing()==True and (counter <9):
            player_move()
            counter+=1
            if keep_playing()==True and (counter <9):
                pass
            else:
                print ("You win!")
                return False
        elif keep_playing()==False:
            print("I win!")
            return False
        elif counter >= 9:
            print ("Draw!")
            return False

#Main component that executes the whole program
while True: 
    board=["1","2","3","4","5","6","7","8","9"]
    if player_confirmation()==True:
        order_chosen=False
        while order_chosen==False:
            goes_first=input ("Would you like to go first?  ").strip().capitalize()
            if goes_first=="Yes":
                ttt_player_first()
                order_chosen=True
            elif goes_first=="No":
                ttt_computer_first()
                order_chosen=True
            else:
                print ("""Input invalid! Please respond with "Yes" or "No".""")
    del winning_square[:]
    del urgent_square[:]
    del other_square[:]
    input("")

    



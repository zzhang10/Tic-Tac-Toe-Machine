
#========================================================================================#
#                                                                                        #
#                               THE TIC TAC TOE MACHINE                                  #
#                                                                                        #
#                                     BY ZACK ZHANG                                      #
#                                                                                        #
#========================================================================================#


#Graphics:
u="⛶" #unplaced
b="⚫" #black piece
w="⚪" #white piece
grid=["placeholder",u,u,u,\
                    u,u,u,\
                    u,u,u] 
label=["Grid numbers:","➊","➋","➌","➍","➎","➏","➐","➑","➒"] #number indicator



#Display sentences:
display_greeting="This is a game of Tic-Tac-Toe."
display_selection="Enter 1 if you would like to go first, and 2 if you would like to go second: "
display_comp_first="I will go first."
display_player_first="You will go first."
display_piece_type="I will be using black pieces ({}) and you will be using white ones ({}).".format(b,w)+\
                    "We can only place on the empty squares({}).".format(u)
display_invalid_beginning_selection="You may only enter 1 or 2. Please select again."
display_compmove="I will place my piece on {}."
display_playermove="Enter the square that you would like place your piece on, according to the grid numbers: "
display_playermove_occupied="Entry invalid. This square is occupied."
display_playermove_invalid="Entry invalid. You may only pick an integer from 1 to 9."
display_player_move="You place your piece on {}."
display_comp_win="I win!"
display_player_win="You win!"
display_draw="It is a draw!"
display_play_again="Would you like to play again? Enter yes or no: "
display_again_invalid="Selection invalid. You may only enter yes or no."


#Row identifiers for later code:
row1=[1,2,3]
row2=[4,5,6]
row3=[7,8,9]
column1=[1,4,7]
column2=[2,5,8]
column3=[3,6,9]
diag1=[1,5,9]
diag2=[3,5,7]
lines=[row1,row2,row3,column1,column2,column3,diag1,diag2]
field=[1,2,3,4,5,6,7,8,9]


#print_grid generates the current match-up of the tic-tac-toe grid, along with
#the label for player to reference.
def print_grid ():
    print(" ")
    print(16*" "+"Game board:")
    print(20*" "+grid[1]+grid[2]+grid[3])
    print(20*" "+grid[4]+grid[5]+grid[6])
    print(20*" "+grid[7]+grid[8]+grid[9])
    print(" ")
    print(16*" "+label[0])
    print(20*" "+label[1]+label[2]+label[3])
    print(20*" "+label[4]+label[5]+label[6])  
    print(20*" "+label[7]+label[8]+label[9])
    print(" ")

#check_endgame checks whether the game has ended in a win or a draw.
def check_endgame():
    win=False
    for line in lines:
        linecheck=[grid[line[0]],grid[line[1]],grid[line[2]]]
        if linecheck == [b,b,b]:
            print (display_comp_win)
            win=True
            return True
        elif linecheck == [w,w,w]:
            print (display_player_win)
            win=True
            return True
    if win==False:
        draw=True
        for square in field:
            if grid[square]==u:
                draw=False
                return False
        if draw==True:
            print(display_draw)
            return True
    else:
        return False
    
#comp_move generates the computer's move against the player       
def comp_move():
    win=[]
    block=[]
    fork=[]
    block_fork=[]
    center=[]
    opposite_corner=[]
    empty_corner=[]
    empty_square=[]
    def row_check (square):
        fork_count=0
        opponent_forkcount=0
        if grid[square] == u:
            for line in lines:
                if square in line:
                    linesort=sorted([grid[line[0]],grid[line[1]],grid[line[2]]])
                    if linesort==[b,b,u]:
                        win.append(square)
                    elif linesort==[w,w,u]:
                        block.append(square)
                    elif linesort==[b,u,u]:
                        fork_count+=1
                    elif linesort==[w,u,u]:
                        opponent_forkcount+=1
        if fork_count >=2:
            fork.append(square)
        elif opponent_forkcount >= 2:
            block_fork.append(square)
    def corner_check (square):
        if square in [1,3,7,9]:
            if grid[square]==u:
                empty_corner.append(square)
            if grid[square]==w:
                if grid [10-square]==u:
                    opposite_corner.append(
                        10-square)
    if grid[5]==u:
        center.append(5)
    for square in field:
        row_check(square)
        corner_check(square)
        if grid[square]==u:
            empty_square.append(square)
    move="undecided"
    if win != []:
        move=win[0]
    elif block != []:
        move=block[0]
    elif fork != []:
        move=fork[0]        
    elif block_fork != []:
        move=block_fork[0]
    elif center != []:
        move=center[0]
    elif opposite_corner != []:
        move=opposite_corner[0]
    elif empty_corner != []:
        move=empty_corner[0]
    else:
        move=empty_square[0]
    print (display_compmove.format(move))
    grid[move]=b
    print_grid()
    endgame=check_endgame()
    if endgame==False:
        player_move()

#player_move prompts the player to make a move.
def player_move():
    move_chosen=False
    while move_chosen==False:
        move=input(display_playermove)
        if move in ["1","2","3","4","5","6","7","8","9"]:
            if grid [int(move)]==u:
                move_chosen=int(move)
            else:
                print(display_playermove_occupied)
        else:
            print(display_playermove_invalid)
    print(display_player_move.format(move_chosen))
    grid[move_chosen]=w
    print_grid()
    endgame=check_endgame()
    if endgame==False:
        comp_move()

#begin_game sets up the initiation of the game
def begin_game ():
    selected=False
    print_grid()
    print(display_greeting)
    while selected == False:
        selection = input (display_selection)
        if selection =="1":
            print(display_piece_type)
            print (display_player_first)
            selected=True
            player_move()
        elif selection == "2":
            print(display_piece_type)
            print (display_comp_first)
            selected=True
            comp_move()
        else:
            print (display_invalid_beginning_selection)



#Main sequence of the game:
begin_game()               
again=True
while again==True:
    play_again=input(display_play_again)
    if play_again.lower()=="no":
        again=False
    elif play_again.lower()=="yes":
        grid=["placeholder",u,u,u,\
                            u,u,u,\
                            u,u,u]
        begin_game()
    else:
        print (display_again_invalid)
    
                    



def print_board():
    print ("               "+ str(board[0]) +" | " +str(board[1]) +" | " +str(board[2]))
    print ("               "+ "---------")
    print ("               "+ str(board[3]) +" | " +str(board[4]) +" | " +str(board[5]))
    print ("               "+ "---------")
    print ("               "+ str(board[6]) +" | " +str(board[7]) +" | " +str(board[8]))
              
def player_confirmed ():
    print("""You will be playing Tic-Tac-Toe against a machine.
    This will be your checkerboard.
    Enter the corresponding number in each of the grids to place your piece.
    I will be using "O" and you will be using "X".""")
    print_board()
    sequence="unknown"
    while sequence == "unknown":
        confirmation=input ("""Please confirm you know the rules by typing "Yes".""").strip().capitalize()
        if confirmation=="Yes":
            print ("You will go first.")
            sequence=="known"
            return True
            break
        elif confirmation=="No":
            print ("You will not be able to enter the match.")
            sequence=="known"
            return False
            break
        else:
            print ("""Response invalid! You may only enter "Yes" or "No".""")

def player_move():
    valid=False
    while valid==False:
        entry=(input ("Enter the number where you would like to place the piece:  ").strip())
        if entry not in ["1","2","3","4","5","6","7","8","9"]:
            print ("Entry invalid! You must enter a number between 1 and 9 that corresponds with the spots on the board.")
        else:
            if int(entry) not in board:
                print ("The spot you have chosen has already been taken. Choose another spot.")
            else:
                entry=int(entry)
                board[entry-1]="X"
                print ("You place your piece on " + str(entry)+"." )
                print_board()
                valid=True
                return entry
                print ("My turn.")
def computer_move(number):
        print ("I will put my piece on " + str(number) + ".")
        board[number-1]="O"
        print_board()
        print ("Your turn.")
def computer_wins(number):
        print ("I will put my piece on " + str(number) + ".")
        board[number-1]="O"
        print_board()
        print ("I win!")
def draw():
    print ("It is a draw!")

def three_step_algo(first,second,third):
    computer_move(first)
    number=player_move()
    if number!=second:
        computer_wins(second)
    else:
        computer_move(third)
        player_move()
        draw()
def six_step_algo(M1,M2,M3,M4,M5,M6):
    computer_move (M1)
    number=player_move()
    if number==M2:
        three_step_algo(M3,M4,M5)
    elif number==M5:
        three_step_algo(M4,M3,M2)
    elif number==M4:
        computer_move(M5)
        number=player_move()
        if number==M2:
            computer_move(M3)
            player_move()
            draw()
        else:
            computer_move(1)
            player_move()
            draw()
    elif number==M6:
        computer_move(M5)
        number=player_move()
        if number==M3:
            computer_move(M1)
            player_move()
            draw()
        else:
            computer_move(M3)
            player_move()
            draw()
    else:
        computer_move(M2)
        number=player_move()
        if number==M5:
            computer_move(M4)
            player_move()
            draw()
        else:
            computer_move(M5)
            player_move()
            draw()                   

def five_step_algo(CM1,CP1,CM2,CP2,CM3):
    computer_move (CM1)
    number=player_move()
    if number !=CP1:
        computer_wins (CP1)
    else:
        computer_move(CM2)
        number=player_move()
        if number !=CP2:
            computer_wins(CP2)
        else:
            computer_move(CM3)
            player_move()
            draw()
def five_step_algo2(first,second,third,fourth,fifth):
    computer_move(first)
    number=player_move()
    if number !=second:
        computer_wins(second)
    else:
        computer_move(third)
        number=player_move()
        if number==fourth:
            computer_move(fifth)
            player_move()
            draw()
        elif number==fifth:
            computer_move(fourth)
            player_move()
            draw()
        else:
            computer_move(fifth)
            player_move()
            draw()
def ttt():
    if player_confirmed()==True:
        number=player_move()
        if number==1:
            computer_move(5)
            number=player_move()
            if number==2:
                five_step_algo(3,7,4,6,9)
            elif number==3:
                five_step_algo(2,8,6,4,7)
            elif number==4:
                five_step_algo(7,3,2,6,9)
            elif number==6:
                five_step_algo(8,2,3,7,4)
            elif number==7:
                five_step_algo(4,6,8,2,3)
            else:# number == [8,9]
                five_step_algo(6,4,7,3,2)                
        elif number==2:
            computer_move(5)
            number=player_move()
            if number==1:
                five_step_algo(3,7,4,6,9)
            elif number==3:
                five_step_algo(1,9,6,4,8)
            elif number==4:
                five_step_algo(1,9,3,7,8)
            elif number==6:
                five_step_algo(3,7,1,9,8)
            elif number==7:
                five_step_algo(6,4,1,9,8)
            elif number==8:
                computer_move(3)
                number=player_move()
                if number !=7:
                    computer_wins(7)
                else:
                    computer_move(9)
                    number=player_move()
                    if number !=1:
                        computer_wins(1)
                    else:
                        computer_wins(6)
            else:
                five_step_algo(4,6,3,7,8)                
        elif number==3:
            computer_move(5)
            number=player_move()
            if number==6:
                five_step_algo(9,1,2,8,7)
            elif number==9:
                five_step_algo(6,4,8,2,1)
            elif number==2:
                five_step_algo(2,9,6,8,7)
            elif number==8:
                five_step_algo(4,6,9,1,2)
            elif number==1:
                five_step_algo(2,8,4,6,9)
            else:# number == [4,7]
                five_step_algo(8,2,1,9,6)                
        elif number==4:
            computer_move(5)
            number=player_move()
            if number==7:
                five_step_algo(1,9,8,2,3)
            elif number==1:
                five_step_algo(7,3,2,8,6)
            elif number==8:
                five_step_algo(7,3,1,9,6)
            elif number==2:
                five_step_algo(1,9,7,3,6)
            elif number==9:
                five_step_algo(2,8,7,3,6)
            elif number==6:
                computer_move(1)
                number=player_move()
                if number !=9:
                    computer_wins(9)
                else:
                    computer_move(3)
                    number=player_move()
                    if number !=7:
                        computer_wins(7)
                    else:
                        computer_wins(2)
            else:
                five_step_algo(8,2,1,9,6)            
        elif number==5:
            computer_move(3)
            number=player_move()
            if number ==1:
                five_step_algo2(9,6,4,2,8)
            elif number ==2:
                six_step_algo(8,1,9,6,4,7)
            elif number ==4:
                five_step_algo(6,9,1,2,8)
            elif number ==6:
                six_step_algo(4,9,1,2,8,7)
            elif number ==7:
                five_step_algo2(9,6,4,2,8)
            elif number ==8:
                five_step_algo(2,1,9,6,4)
            else:
                five_step_algo2(1,4,6,8,2)                
        elif number==6:
            computer_move(5)
            number=player_move()
            if number==3:
                five_step_algo(9,1,2,8,7)
            elif number==9:
                five_step_algo(3,7,8,2,4)
            elif number==2:
                five_step_algo(3,7,9,1,4)
            elif number==8:
                five_step_algo(9,1,3,7,4)
            elif number==1:
                five_step_algo(8,2,3,7,4)
            elif number==4:
                computer_move(9)
                number=player_move()
                if number !=1:
                    computer_wins(1)
                else:
                    computer_move(7)
                    number=player_move()
                    if number !=3:
                        computer_wins(3)
                    else:
                        computer_wins(8)
            else:
                five_step_algo(2,8,9,1,4)                
        elif number==7:
            computer_move(5)
            number=player_move()
            if number==4:
                five_step_algo(1,9,8,2,3)
            elif number==1:
                five_step_algo(4,6,2,8,9)
            elif number==8:
                five_step_algo(9,1,4,2,3)
            elif number==2:
                five_step_algo(6,4,1,9,8)
            elif number==9:
                five_step_algo(8,2,6,4,1)
            else:# number == [6,3]
                five_step_algo(2,8,9,1,4)                
        elif number==8:
            computer_move(5)
            number=player_move()
            if number==9:
                five_step_algo(7,3,6,4,1)
            elif number==7:
                five_step_algo(9,1,4,6,2)
            elif number==6:
                five_step_algo(9,1,7,3,2)
            elif number==4:
                five_step_algo(7,3,9,1,2)
            elif number==3:
                five_step_algo(4,6,9,1,2)
            elif number==2:
                computer_move(7)
                number=player_move()
                if number !=3:
                    computer_wins(3)
                else:
                    computer_move(1)
                    number=player_move()
                    if number !=9:
                        computer_wins(9)
                    else:
                        computer_wins(4)
            else:
                five_step_algo(6,4,7,3,2)              
        else:
            computer_move(5)
            number=player_move()
            if number==8:
                five_step_algo(7,3,6,4,1)
            elif number==7:
                five_step_algo(8,2,4,6,3)
            elif number==6:
                five_step_algo(3,7,8,4,1)
            elif number==4:
                five_step_algo(2,8,7,3,6)
            elif number==3:
                five_step_algo(6,4,2,8,7)
            else:# number == [2,1]
                five_step_algo(4,6,3,7,8)        
    else:
        print ("Go play Grand Theft Auto instead.")  
while True:
    board=[1,2,3,4,5,6,7,8,9]
    ttt()
    input()


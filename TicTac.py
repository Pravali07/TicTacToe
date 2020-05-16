class Board:
    def __init__(self):
       print('Welcome to Tic Tac Toe')
       self.board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
       self.player1=''
       self.player2=''
       self.player= True
       self.again = ''
    def display_board(self):
        print('   |   |')
        print(' '+self.board[1]+' | '+self.board[2]+' | '+self.board[3])
        print('-----------')
        print('   |   |')
        print(' '+self.board[4]+' | '+self.board[5]+' | '+self.board[6])
        print('-----------')
        print('   |   |')
        print(' '+self.board[7]+' | '+self.board[8]+' | '+self.board[9])
    def get_move(self):
        x=len(self.board)
        while(x != 1):
            if self.player == True: print('Your move Player1(1-9):')
            else: print('Your move Player2(1-9):')
            try:
                move = int(input())
                if move >=1 and move <=9:
                    if self.board[move] == ' ':
                        if self.player == True:
                            self.board[move] = self.player1
                            self.player = False
                            self.display_board()
                            x-=1
                        elif self.player == False:
                            self.board[move] = self.player2
                            self.player = True
                            self.display_board()
                            x-=1
                    else:
                        print('Already filled!!Select another one')
                else:
                    print('Invalid move')
            except:
                print ('Invalid move')
            if x <= 5:
                if self.board[1] == self.board[2] == self.board[3] != ' ':
                    print("Game Over")
                    if self.player == False:print("Player1 won the game")
                    if self.player== True:print("Player2 won the game")
                    break
                elif self.board[1] == self.board[4] == self.board[7] != ' ':
                    print("Game Over")
                    if self.player == False: print("Player1 won the game")
                    if self.player == True:print("Player2 won the game")
                    break
                elif self.board[2] == self.board[5] == self.board[8] != ' ':
                    print("Game Over")
                    if self.player == False: print("Player1 won the game")
                    if self.player == True:print("Player2 won the game")
                    break
                elif self.board[4] == self.board[5] == self.board[6] != ' ':
                    print("Game Over")
                    if self.player == False: print("Player1 won the game")
                    if self.player == True:print("Player2 won the game")
                    break
                elif self.board[7] == self.board[8] == self.board[9] != ' ':
                    print("Game Over")
                    if self.player == False: print("Player1 won the game")
                    if self.player == True:print("Player2 won the game")
                    break
                elif self.board[3] == self.board[6] == self.board[9] != ' ':
                    print("Game Over")
                    if self.player == False: print("Player1 won the game")
                    if self.player == True:print("Player2 won the game")
                    break
                elif self.board[1] == self.board[5] == self.board[9] != ' ':
                    print("Game Over")
                    if self.player == False: print("Player1 won the game")
                    if self.player == True:print("Player2 won the game")
                    break
                elif self.board[3] == self.board[5] == self.board[7] != ' ':
                    print("Game Over")
                    if self.player == False: print("Player1 won the game")
                    if self.player == True:print("Player2 won the game")
                    break
            if x == 1:
                print("Game Over")
                print("It's a tie")
                break
        self.again = input("Do u wanna play again?(y/n)")
        if self.again == 'y' or self.again == 'Y':
            b=Board()
            b.display_board()
            b.player_name()
            b.get_move()
    def player_name(self):
        while not(self.player1 == 'X' or self.player1 == 'O'):
            print('What do u want? X or O')
            self.player1=input().upper()
        if self.player1 == 'X':
            self.player2= 'O'
        else:
            self.player2= 'X'
        print('Player 1-',self.player1)
        print('Player 2-',self.player2)
            

b=Board()
b.display_board()
b.player_name()
b.get_move()

        

    




def print_board(board):
    print()
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")
    print()

def is_win(board,symbol):
    #same row 
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True
    
    #same Column
    for j in range(3):
        if board[0][j] == symbol and board[1][j] == symbol and board[2][j] == symbol:
            return True
    
    #same diagonal
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True

    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    #if all case fails
    return False


def is_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True



def get_input(mark,id):
    while True:
        try:
            move = input(f"Player{id}, Enter the position to place {mark}->  ")
            ip = move.strip().split()

            if len(ip) != 2:
                print("Enter exactly 2 coordinates!")
                continue

            row,col = int(ip[0]),int(ip[1])

            if (row>=1 and row<= 3) and (col>=1 and col<=3):
                return [row-1,col-1]
            else:
                print("Enter values between 1 and 3 only")
        except ValueError:
            print("Invalid inputs, enter numbers only")


board = []
for i in range(3):
    board.append([" "," "," "])

mark1 = "X"
mark2 = "O"
p1 = 1
p2 = 2
curr_p = 1
curr_m = "X"
while True:
    print_board(board)
    row,col = get_input(curr_m,curr_p)

    if board[row][col] != " ":
        print("Move already taken!,Try again")
        continue

    board[row][col] = curr_m

    if is_win(board,curr_m):
        print_board(board)
        print(f"Congrats🎉, Player{curr_p} wins!!!")
        break

    if is_draw(board):
        print_board(board)
        print("Its a draw,🫡!")
        break

    if curr_p == p1:
        curr_p = p2
        curr_m = "O"
    else:
        curr_p = p1
        curr_m = "X"

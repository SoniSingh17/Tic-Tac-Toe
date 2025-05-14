print("Welcome to Tic Tac Toe...")

board = ["0", "1", "2",
         "3", "4", "5",
         "6", "7", "8"]

currPlayer = "X"
gamerunning = True

# Print the board
def Print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("---|---|---")

# Player input
def playerInput(board):
    global currPlayer
    choice = int(input(f"Enter your choice {currPlayer} (0-8): "))
    if 0 <= choice <= 8 and board[choice] == str(choice):
        board[choice] = currPlayer
    else:
        print("Invalid move. Try again.")
        playerInput(board)

# Winner check
def win(board):
    win_cond = [(0,1,2), (3,4,5), (6,7,8),  # horizontal
                (0,3,6), (1,4,7), (2,5,8),  # vertical
                (0,4,8), (2,4,6)]           # diagonal

    for x, y, z in win_cond:
        if board[x] == board[y] == board[z]:
            print("Winner is " + board[x])
            return True
    return False

# Tie check
def tiecheck(board):
    if all(cell in ["X", "O"] for cell in board):
        print("It's a tie!")
        return True
    return False

# Toggle player
def toggle_player():
    global currPlayer
    if currPlayer == "X":
        currPlayer = "O"
    else:
        currPlayer = "X"

# Main game loop
while gamerunning:
    Print_board(board)
    playerInput(board)
    if win(board):
        Print_board(board)
        gamerunning = False
        break
    if tiecheck(board):
        Print_board(board)
        gamerunning = False
        break
    toggle_player()

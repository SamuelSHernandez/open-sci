def print_board(board):
    for row in board:
        for col in row:
            print(col, end=' ')
        print()

def check_win(board):
    # Horizontal win
    for row in board:
        if row[0] == row[1] == row[2] != '.':
            return True

    return next(
        (
            True
            for col in range(3)
            if board[0][col] == board[1][col] == board[2][col] != '.'
        ),
        True
        if board[0][0] == board[1][1] == board[2][2] != '.'
        else board[0][2] == board[1][1] == board[2][0] != '.',
    )

def print_winner(score):
    if len(score) > 0:
        print("Congratulations! The winner is:", score[-1])
    else:
        print("It's a tie! No winner.")

def play_again():
    answer = input("Do you want to play again? (Y/N): ")
    return answer.upper() == "Y"

while True:
    board = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ]
    score = []
    win = False

    print("Welcome to Tic-Tac-Toe!")
    print("Player 1: X | Player 2: O")
    print("Let's start!")

    print_board(board)
    while not win:
        p1_row, p1_col = input('Player 1 - Select row and column of your move (separated by a comma):').split(",", 1)
        board[int(p1_row) - 1][int(p1_col) - 1] = "X"
        print_board(board)
        if check_win(board):
            win = True
            score.append('Player 1')
            print_winner(score)
            if play_again():
                break
            else:
                quit()

        if not win:
            p2_row, p2_col = input('Player 2 - Select row and column of your move (separated by a comma):').split(",", 1)
            board[int(p2_row) - 1][int(p2_col) - 1] = "O"
            print_board(board)
            if check_win(board):
                win = True
                score.append('Player 2')
                print_winner(score)
                if play_again():
                    break
                else:
                    quit()

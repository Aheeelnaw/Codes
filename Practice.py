def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        print(f"Player {players[turn % 2]}'s turn. Enter row (1-3) and column (1-3) separated by space:")
        row, col = map(int, input().split())

        if board[row-1][col-1] == ' ':
            board[row-1][col-1] = players[turn % 2]

            if check_win(board, players[turn % 2]):
                print_board(board)
                print(f"Player {players[turn % 2]} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            turn += 1
        else:
            print("That spot is already taken. Try again.")

if __name__ == "__main__":
    main()

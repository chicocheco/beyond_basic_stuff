# tictactoe.py, A non-OOP tic-tac-toe game.
ALL_SPACES = list('123456789')  # The keys for a TTT board dictionary.
X, O, BLANK = 'X', 'O', ' '  # Constants for string values.


def main():
    """Runs a game of tic-tac-toe."""

    print('Welcome to tic-tac-toe!')
    game_board = get_blank_board()  # Create a TTT board dictionary.
    current_player, next_player = X, O  # X goes first, O goes next.
    while True:
        print(get_board_str(game_board))
        # Display the board on the screen.
        # Keep asking the player until they enter a number 1-9:
        move = None
        while not is_valid_space(game_board, move):
            print(f'What is {current_player}\'s move? (1-9)')
            move = input()
        update_board(game_board, move, current_player)  # Make the move.
        # Check if the game is over:
        if is_winner(game_board, current_player):  # First check for victory.
            print(get_board_str(game_board))
            print(f'{current_player} has won the game!')
            break
        elif is_board_full(game_board):  # Next check for a tie.
            print(get_board_str(game_board))
            print('The game is a tie!')
            break
        current_player, next_player = next_player, current_player  # Swap turns.
    print('Thanks for playing!')


def get_blank_board():
    """Create a new, blank tic-tac-toe board."""
    board = {}  # The board is represented as a Python dictionary.
    for space in ALL_SPACES:
        board[space] = BLANK  # All spaces start as blank.
    return board


def get_board_str(board):
    """Return a text-representation of the board."""

    return f'''
        {board['1']}|{board['2']}|{board['3']} 1 2 3
        -+-+-
        {board['4']}|{board['5']}|{board['6']} 4 5 6
        -+-+-
        {board['7']}|{board['8']}|{board['9']} 7 8 9'''


def is_valid_space(board, space):
    """Returns True if the space on the board is a valid space number
    and the space is blank."""
    return space in ALL_SPACES and board[space] == BLANK


def is_winner(board, player):
    """Return True if player is a winner on this TTTBoard."""

    b, p = board, player  # Shorter names as "syntactic sugar".
    # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
    return ((b['1'] == b['2'] == b['3'] == p) or  # Across the top
            (b['4'] == b['5'] == b['6'] == p) or  # Across the middle
            (b['7'] == b['8'] == b['9'] == p) or  # Across the bottom
            (b['1'] == b['4'] == b['7'] == p) or  # Down the left
            (b['2'] == b['5'] == b['8'] == p) or  # Down the middle
            (b['3'] == b['6'] == b['9'] == p) or  # Down the right
            (b['3'] == b['5'] == b['7'] == p) or  # Diagonal
            (b['1'] == b['5'] == b['9'] == p))  # Diagonal


def is_board_full(board):
    """Return True if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # If a single space is blank, return False.
    return True  # No spaces are blank, so return True.


def update_board(board, space, mark):
    """Sets the space on the board to mark."""
    board[space] = mark


if __name__ == '__main__':
    main()  # Call main() if this module is run, but not when imported.

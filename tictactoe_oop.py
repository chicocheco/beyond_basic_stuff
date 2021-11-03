# tictactoe_oop.py, an object-oriented tic-tac-toe game.
import copy

ALL_SPACES = list('123456789')  # The keys for a TTT board.
X, O, BLANK = 'X', 'O', ' '  # Constants for string values.


def main():
    """Runs a game of tic-tac-toe."""
    print('Welcome to tic-tac-toe!')
    # if input('Use mini board? Y/N: ').lower().startswith('y'):
    #     game_board = MiniBoard()  # Create a MiniBoard object.
    # else:
    #     game_board = TTTBoard()  # Create a TTTBoard object.
    # game_board = HintBoard()
    game_board = HybridBoard()
    current_player, next_player = X, O  # X goes first, O goes next.
    while True:
        print(game_board.get_board_str())
        # Display the board on the screen.
        # Keep asking the player until they enter a number 1-9:
        move = None
        while not game_board.is_valid_space(move):
            print(f'What is {current_player}\'s move? (1-9)')
            move = input()
        game_board.update_board(move, current_player)  # Make the move.
        # Check if the game is over:
        if game_board.is_winner(current_player):  # First check for victory.
            print(game_board.get_board_str())
            print(f'{current_player} has won the game!')
            break
        elif game_board.is_board_full():  # Next check for a tie.
            print(game_board.get_board_str())
            print('The game is a tie!')
            break
        current_player, next_player = next_player, current_player  # Swap turns.
    print('Thanks for playing!')


class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):

        """Create a new, blank tic tac toe board."""
        self._spaces = {}  # The board is represented as a Python dictionary.
        for space in ALL_SPACES:
            self._spaces[space] = BLANK  # All spaces start as blank.

    def get_board_str(self):
        """Return a text-representation of the board."""
        return f'''
    {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']}
    -+-+-
    {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']}
    -+-+-
    {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']}
    1 2 3
    4 5 6
    7 8 9'''

    def is_valid_space(self, space):
        """Returns True if the space on the board is a valid space number
        and the space is blank."""
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def is_winner(self, player):
        """Return True if player is a winner on this TTTBoard."""
        s, p = self._spaces, player  # Shorter names as "syntactic sugar".
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
        return ((s['1'] == s['2'] == s['3'] == p) or  # Across the top
                (s['4'] == s['5'] == s['6'] == p) or  # Across the middle
                (s['7'] == s['8'] == s['9'] == p) or  # Across the bottom
                (s['1'] == s['4'] == s['7'] == p) or  # Down the left
                (s['2'] == s['5'] == s['8'] == p) or  # Down the middle
                (s['3'] == s['6'] == s['9'] == p) or  # Down the right
                (s['3'] == s['5'] == s['7'] == p) or  # Diagonal
                (s['1'] == s['5'] == s['9'] == p))  # Diagonal

    def is_board_full(self):
        """Return True if every space on the board has been taken."""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False  # If a single space is blank, return False.
        return True  # No spaces are blank, so return True.

    def update_board(self, space, player):
        """Sets the space on the board to player."""
        self._spaces[space] = player


class MiniBoard(TTTBoard):
    """Child classes inherit all the methods of their parent classes. But a child
    class can override an inherited method by providing its own method with
    its own code. The child class’s overriding method will have the same name
    as the parent class’s method."""

    def get_board_str(self):
        """Return a tiny text-representation of the board."""
        # Change blank spaces to a '.'
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                self._spaces[space] = '.'
        board_str = f'''
        {self._spaces['1']}{self._spaces['2']}{self._spaces['3']} 123
        {self._spaces['4']}{self._spaces['5']}{self._spaces['6']} 456
        {self._spaces['7']}{self._spaces['8']}{self._spaces['9']} 789'''
        # Change '.' back to blank spaces.
        for space in ALL_SPACES:
            if self._spaces[space] == '.':
                self._spaces[space] = BLANK
        return board_str


class HintBoard(TTTBoard):
    """A child class’s overridden method is often similar to the parent class’s
    method. Even though inheritance is a code reuse technique, overriding
    a method might cause you to rewrite the same code from the parent class’s
    method as part of the child class’s method.

    To prevent this duplicate code, the built-in super() function allows an overriding method to call the original
    method in the parent class."""

    def get_board_str(self):
        """Return a text-representation of the board with hints."""
        board_str = super().get_board_str()  # Call getBoardStr() in TTTBoard.
        x_can_win = False
        o_can_win = False
        original_spaces = self._spaces  # Backup _spaces.
        for space in ALL_SPACES:  # Check each space:
            # Simulate X moving on this space:
            self._spaces = copy.copy(original_spaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.is_winner(X):
                x_can_win = True
            # Simulate O moving on this space:
            self._spaces = copy.copy(original_spaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.is_winner(O):
                o_can_win = True
        if x_can_win:
            board_str += '\nX can win in one more move.'
        if o_can_win:
            board_str += '\nO can win in one more move.'
        self._spaces = original_spaces
        return board_str


class HybridBoard(HintBoard, MiniBoard):
    """Multiple inheritance with no code whose only purpose is to combine a mini board with hints.
        When we call get_board_str() on a HybridBoard object, Python knows that
    the HybridBoard class doesn’t have a method with this name, so it checks
    its parent class. But which of the two parent classes gets called? Let's check the MRO.

    METHOD RESOLUTION ORDER
    -----------------------
    HybridBoard.mro()
    [<class 'tictactoe_oop.HybridBoard'>, <class 'tictactoe_oop.HintBoard'>,
    <class 'tictactoe_oop.MiniBoard'>, <class 'tictactoe_oop.TTTBoard'>, <class 'object'>]

    - Python checks child classes before parent classes.
    - Python checks inherited classes listed left to right in the class statement.

    Python’s super() function doesn’t return the parent class but rather the next class in the MRO.
    The call to super().get_board_str() in HintBoard in this case calls the MiniBoard class’s get_board_str() method
    (not the parent class TTTBoard!).
    """
    pass


if __name__ == '__main__':
    main()  # Call main() if this module is run, but not when imported.

"""
this class handles Console prints and visuals of the game
"""

from colorama import init 
from colorama import Fore, Back, Style
from game_state import game_state
from pieces import Piece

class Display:
    def __init__(self):
        init()


    def draw(self):
        print('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n')
        print(15*' ' + '.     a   b   c   d   e   f   g   h') 
        print('') 
        print('')
        for row in range(len(game_state.board)):
            print(Fore.WHITE + 15*' ' + str(row + 1) + '    ' + " ".join(self.get_string(game_state.board[row][column], (row, column)) for column in range(len(game_state.board[row]))) + Fore.WHITE + 15*' ')
            print('')
        print('\n \n \n \n \n \n')
        

    def get_string(self, piece: Piece, position: tuple):
        if int(piece[1]) == 1:
            return Fore.RED + f' {self.get_char(piece[0], position)} '
        elif int(piece[1]) == 2:
            return Fore.WHITE + f' {self.get_char(piece[0], position)} '
        return Fore.WHITE + f' {self.get_char(piece[0], position)} '
    

    def get_char(self, piece_num: int, position: tuple):
        color = Fore.YELLOW if game_state.requests['valid_moves']['requested'] \
            and position in game_state.requests['valid_moves']['value'] else Fore.WHITE
        return {
            1: 'P',
            2: 'N',
            3: 'B',
            4: 'R', 
            5: 'Q',
            6: 'K'
        }.get(piece_num, color + '.' + Fore.WHITE)
    

    def show_valid_moves(self, moves):
        pass



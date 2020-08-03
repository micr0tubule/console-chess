"""
this class handles Console prints and visuals of the game
"""

from game_state import game_state
from pieces import Piece
from curses import * 
import time

class Display:

    def draw(self):
        y_offset = 2
        x_offset = 4
        stdscr = initscr()
        start_color()
        init_pair(1, 7, 0) # white
        init_pair(2, 4, 0) # red
        init_pair(3, 3, 0) # yellow
        stdscr.addstr(0, 6, 'a   b   c   d   e   f   g   h')
        for row in range(8):
            for column in range(8):      
                stdscr.addstr(row * y_offset + 3, 0, str(row + 1))
                stdscr.addstr(row * y_offset + 3, column * x_offset + 6, \
                    self.get_char(game_state.board[row][column]), self.get_color(game_state.board[row][column])) 
                stdscr.refresh()


    def get_char(self, piece: tuple):
        return {
            1: 'P',
            2: 'N',
            3: 'B',
            4: 'R', 
            5: 'Q',
            6: 'K'
        }.get(piece[0], '.')
    

    def get_color(self, piece: tuple):

        if has_colors(): 
            if game_state.requests['valid_moves']['requested'] and position in game_state.requests['valid_moves']['value']: 
                return color_pair(3)

            return color_pair(2) if piece[1] == 1 else color_pair(1)
        return start_color(1)
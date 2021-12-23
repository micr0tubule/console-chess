
import numpy
from party import Party

class GameState:
    def __init__(self):
        self.its_whites_turn = False # False for red party True for white party
        self.red_party = Party()
        self.white_party = Party(inverse=True)
        self.current_party = self.red_party
        self.board = numpy.zeros((8, 8, 2))
        self.requests = {
            'valid_moves': {'requested': False, 'value': []}
            }
        for piece in self.red_party.pieces + self.white_party.pieces:
            self.board[piece.position[0], piece.position[1]][0] = int(piece) 
            self.board[piece.position[0], piece.position[1]][1] = piece.party


    def get_non_current_party(self): 
        '''
        returns the party that is not the current party
        '''
        return self.white_party if self.current_party is self.red_party else self.red_party 
    

    def apply(self): 
        '''
        apply changes to board 
        '''
        self.board = numpy.zeros((8, 8, 2))
        for piece in self.red_party.pieces + self.white_party.pieces:
            self.board[piece.position[0], piece.position[1]][0] = int(piece) 
            self.board[piece.position[0], piece.position[1]][1] = piece.party        

game_state = GameState()
        

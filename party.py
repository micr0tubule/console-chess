'''
represents the player 
keeps inventory of pieces of player and handles actions 
'''

from pieces import Pawn, Knight, Bishop, Rook, Queen, King
import numpy

class Party:
    def __init__(self, inverse=False):
        self.inverse = inverse
        if not inverse: 
            self.pieces = [Pawn(position=(1, i)) for i in range(8)]
            self.pieces.append(Rook(position=(0, 0)))
            self.pieces.append(Knight(position=(0, 1)))
            self.pieces.append(Bishop(position=(0, 2)))
            self.pieces.append(Queen(position=(0, 3)))
            self.pieces.append(King(position=(0, 4)))
            self.pieces.append(Bishop(position=(0, 5)))
            self.pieces.append(Knight(position=(0, 6)))
            self.pieces.append(Rook(position=(0, 7)))
        else: 
            self.pieces = [Pawn(position=(6, i), party=2) for i in range(8)]
            self.pieces.append(Rook(position=(7, 0), party=2))
            self.pieces.append(Knight(position=(7, 1), party=2))
            self.pieces.append(Bishop(position=(7, 2), party=2))
            self.pieces.append(Queen(position=(7, 3), party=2))
            self.pieces.append(King(position=(7, 4), party=2))
            self.pieces.append(Bishop(position=(7, 5), party=2))
            self.pieces.append(Knight(position=(7, 6), party=2))
            self.pieces.append(Rook(position=(7, 7), party=2))
        

    def move(self, piece, destination):
        for pie in self.pieces: 
            if pie.position == piece.position:
                pie.position = destination
                return


    def find_piece(self, position):
        for piece in self.pieces:
            if piece.position == position: return piece
        return False


    def get_position(self, piece_num):
        return {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7, 
            'h': 8
        }.get(piece_num, False)
 

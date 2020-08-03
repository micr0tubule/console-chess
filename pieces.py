from enum import Enum


class Piece: 
    def __init__(self, position, party=1):
        self.position = position
        self.party = party
    
    def get_moves(self, from_position, position_is_empty): 
        return None

class Pawn(Piece):
    def __init__(self, position, party=1):
        super().__init__(position, party)

    def __int__(self):
        return 1
        
    def get_valid_moves(self, position_is_empty):
        '''
        '''
        moves = []    
        forward_move = (self.position[0] + 1 if self.party == 1 else self.position[0] -1, self.position[1])

        if position_is_empty(forward_move, self.party): 
            moves.append(forward_move)
        return moves

class Knight(Piece):
    def __init__(self, position, party=1): 
        super().__init__(position, party)
    
    def __int__(self):
        return 2

    def get_valid_moves(self, position_is_empty): 
        moves = []
        moves.append((self.position[0] - 2, self.position[1] + 1))
        moves.append((self.position[0] -2, self.position[1] - 1))
        moves.append((self.position[0] + 2, self.position[1] + 1))
        moves.append((self.position[0] + 2, self.position[1] - 1))
        moves.append((self.position[0] + 1, self.position[1] + 2))
        moves.append((self.position[0] + 1, self.position[1] - 2))
        moves.append((self.position[0] - 1, self.position[1] - 2))
        moves.append((self.position[0] - 1, self.position[1] + 2))   
         
        return moves

class Bishop(Piece): 
    def __init__(self, position, party=1):
        super().__init__(position, party)
        
    def __int__(self):
        return 3
    
    def get_valid_moves(self, position_is_empty): 

        def _position_is_empty(position): 
            return position_is_empty(position, self.party)

        moves = []
        
        # right down
        for i in range(8 - self.position[1]):
            moves.append((self.position[0] + i, self.position[1] + i))
            if not _position_is_empty((self.position[0] + i, self.position[1] + i)) and not i == 0:
                break
        # left down
        for i in range(self.position[1] - 1):
            moves.append((self.position[0] + i, self.position[1] - i))
            if not _position_is_empty((self.position[0] + i, self.position[1] - i)) and not i == 0:
                break
        # left up
        for i in range(self.position[1]): 
            moves.append((self.position[0] - i, self.position[1] - i))
            if not _position_is_empty((self.position[0] - i, self.position[1] - i)) and not i == 0:
                break
        # right up
        for i in range(8 - self.position[1]): 
            moves.append((self.position[0] - i, self.position[1] + i))
            if not _position_is_empty((self.position[0] - i, self.position[1] - i)) and not i == 0:
                break
        
        return moves

class Rook(Piece): 
    def __init__(self, position, party=1):
        super().__init__(position, party)
        
    def __int__(self):
        return 4

    
    def get_valid_moves(self, position_is_empty):

        def _position_is_empty(position): 
            return position_is_empty(position, self.party)

        moves = []
        # down
        for i in range(8 - self.position[0]):
            moves.append((i, self.position[1]))
            if not _position_is_empty((i, self.position[1])) and not i == 0:
                break
        # up
        for i in range(self.position[0]): 
            moves.append((i, self.position[1]))
            if not _position_is_empty((i, self.position[1])) and not i == 0:
                break
        # left
        for i in range(8 - self.position[1]): 
            moves.append((self.position[0], i))
            if not _position_is_empty((i, self.position[1])) and not i == 0:
                break
        # right
        for i in range(self.position[1]): 
            moves.append((self.position[0], i))
            if not _position_is_empty((i, self.position[1])) and not i == 0:
                break

        
        return moves

class Queen(Piece): 
    def __init__(self, position, party=1):
        super().__init__(position, party)
            
    def __int__(self):
        return 5

    def get_valid_moves(self, position_is_empty): 

        def _position_is_empty(position): 
            return position_is_empty(position, self.party)

        moves = []
          # down
        for i in range(8 - self.position[0]):
            moves.append((i, self.position[1]))
            if not _position_is_empty((i, self.position[1]),) and not i == 0:
                break
        # up
        for i in range(self.position[0]): 
            moves.append((i, self.position[1]))
            if not _position_is_empty((i, self.position[1]),) and not i == 0:
                break
        # left
        for i in range(8 - self.position[1]): 
            moves.append((self.position[0], i))
            if not _position_is_empty((i, self.position[1]),) and not i == 0:
                break
        # right
        for i in range(self.position[1]): 
            moves.append((self.position[0], i))
            if not _position_is_empty((i, self.position[1]),) and not i == 0:
                break

          # right down
        for i in range(8 - self.position[1]):
            moves.append((self.position[0] + i, self.position[1] + i))
            if not _position_is_empty((self.position[0] + i, self.position[1] + i)) and not i == 0:
                break
        # left down
        for i in range(self.position[1] - 1):
            moves.append((self.position[0] + i, self.position[1] - i))
            if not _position_is_empty((self.position[0] + i, self.position[1] - i)) and not i == 0:
                break
        # left up
        for i in range(self.position[1]): 
            moves.append((self.position[0] - i, self.position[1] - i))
            if not _position_is_empty((self.position[0] - i, self.position[1] - i)) and not i == 0:
                break
        # right up
        for i in range(8 - self.position[1]): 
            moves.append((self.position[0] - i, self.position[1] + i))
            if not _position_is_empty((self.position[0] - i, self.position[1] - i)) and not i == 0:
                break
        
        return moves

class King(Piece):
    def __init__(self, position, party=1):
        super().__init__(position, party)
        
    def __int__(self):
        return 6

    def get_valid_moves(self, position_is_empty):
        moves = []
        # down
        moves.append((self.position[0] + 1, self.position[0]))
        # down right 
        moves.append((self.position[0] + 1, self.position[1] + 1))
        # right
        moves.append((self.position[0], self.position[1] + 1))
        # up right 
        moves.append((self.position[0] - 1, self.position[1] + 1))
        # )
        moves.append((self.position[0] - 1, self.position[1])) 
        # up left
        moves.append((self.position[0] - 1, self.position[1] - 1))
        # left 
        moves.append((self.position[0], self.position[1] - 1))   
        # down left
        moves.append((self.position[0] + 1, self.position[1] - 1))  

        return moves
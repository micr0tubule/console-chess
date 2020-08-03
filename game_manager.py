'''
this class handles actions a player can do 
'''
from enum import Enum
from functools import partial
from display import Display
from game_state import game_state
from pieces import Piece

display = Display()
    
class Action(Enum):
    MOVE = 'move',
    VALID_MOVES = 'valid_moves'

class GameManager:
    '''
    class to handle game state
    ''' 
    def handle_action(self, action: Action):
        '''
        handles action sets players turn 

        '''
        if action: 
            self.modify_state(action)

        game_state.its_whites_turn = not game_state.its_whites_turn if action[0] is Action.MOVE  else game_state.its_whites_turn
        game_state.current_party = game_state.white_party if game_state.its_whites_turn else game_state.red_party
    

    def handle_move(self, piece, destination): 
        attacked_piece = self.check_if_empty(destination, party=game_state.get_non_current_party(), return_piece=True)
        game_state.current_party.move(piece, destination)
        if type(attacked_piece) != bool:  
            game_state.get_non_current_party().pieces.remove(attacked_piece)
        game_state.apply()
 

    def modify_state(self, action: Action):
        '''
        gets validated acion as input and modifies, applies game state
        '''
        {
            Action.MOVE: partial(self.handle_move, action[1], action[2]),
            Action.VALID_MOVES: partial(self.request_valid_moves, action[2])
        }.get(action[0], False)()
        game_state.apply()    

        
    def request_valid_moves(self, valid_moves: list): 
        '''
        sets request in the game state to tell the display to draw the valid moves 
        '''
        game_state.requests['valid_moves']['requested'] = True
        game_state.requests['valid_moves']['value'] = valid_moves


    def request_action(self): 
        actioned = False
        while not actioned: 
            _input = input('white: ') if game_state.its_whites_turn else input('red: ')
            action = self.validate_input(_input)
            actioned = True if action else False
        return action
    

    def validate_input(self, input: str): 
        '''
        filters commands and turns them into actions 
        commands: 
        1. position, !valid moves: position defines a piece, !valid moves command shows what moves the defined piece can take,
        2. position, destination: position defines a piece, destination defines where the player wants to move the defined piece  
        '''        
        position = input.split()[0]
        command = ' '.join(word for word in input.split()[1:])

        # selected piece
        position_x = int(position[0]) 
        position_y = game_state.current_party.get_position(position[1])
        position = (position_x - 1, position_y - 1) if position_y else False

        # 1st command
        if command == '!valid moves':
            piece = game_state.current_party.find_piece(position)
            valid_positions = self.get_valid_positions(piece, position) 
            return (Action.VALID_MOVES, piece, valid_positions) if piece else False 
        
        # 2nd command
        destination_x = int(command[0])
        destination_y = game_state.current_party.get_position(command[1])
        destination = (destination_x - 1, destination_y - 1) if destination_y else False

        if not position_y or not destination_y: 
            return False

        piece = game_state.current_party.find_piece(position)
        if not piece: 
            return False

        valid_positions = self.get_valid_positions(piece, position)        
        print(destination)
        return (Action.MOVE, piece, destination) if destination in valid_positions else False 

    
    def get_valid_positions(self, piece: Piece, position: tuple): 
        '''
        returns all valid moves the piece can do from that position
        '''
        valid_positions = piece.get_valid_moves(self.check_if_empty)
        return self.filter_empty_positions(valid_positions)
    

    def filter_empty_positions(self, positions: list):
        '''
        gets possible positions a piece can move to and checks if they are empty
        '''
        empty_positions = []
        for position in positions:
            empty = True 
            for piece in game_state.current_party.pieces:
                if position == piece.position:
                    empty = False
            if empty: 
                empty_positions.append(position)
        return empty_positions
    

    def check_if_empty(self, position: tuple, party: int, return_piece=False):
        '''
        used in piece objects if they need a special check if a position is empty
        '''
        party = game_state.red_party if party is 1 else game_state.white_party
        for piece in party.pieces:
            if piece.position == position:
                return False if not return_piece else piece
        return True
         
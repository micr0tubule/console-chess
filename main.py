""" 
this file handles the game 
"""

from display import Display
from game_manager import GameManager
from game_state import game_state
# global game state for modifying it and getting values out of it

def main():
    display = Display()
    game_manager = GameManager()
    # game loop
    running = True
    while running: 
        display.draw()
        if game_state.its_whites_turn: 
            game_manager.handle_action(game_manager.request_action())
            display.draw()
        else: 
            game_manager.handle_action(game_manager.request_action())
            display.draw()


if __name__ == '__main__':
    main()